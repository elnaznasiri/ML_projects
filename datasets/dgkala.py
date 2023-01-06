from typing import List, TypedDict
from pymongo import MongoClient
import requests
import configparser

parser = configparser.ConfigParser()
parser.read("connections.conf")

#Create connection to MongoDB
client = MongoClient((parser.get('mongodb_config','hostname')),int(parser.get('mongodb_config','port')))
#Set database name
db = client[parser.get('mongodb_config','database')]
#Set collection name
collection = db[parser.get('mongodb_config','collection')]

# Type definitions
class Reactions(TypedDict):
    likes: int
    dislikes: int


class Comment(TypedDict):
    id: int
    title: str
    body: str
    created_at: str
    rate: int
    reactions: Reactions
    is_buyer: bool
    user_name: str
    is_anonymous: bool


def sendCommentsIntoMongo(json_data):
    for i in range(len(json_data)):
        postID = collection.insert_one(json_data[i])
        #Print ID of inserted document
        print(postID)


def getComment(sess: requests.Session, product_id: int, page: int = 1, pager: bool = False) -> List[Comment]:
    URL = f'https://api.digikala.com/v1/product/{product_id}/comments/?page={page}'
    response = sess.get(URL)

    if response.ok:
        data = response.json().get('data')
        complete_comment = data.get('comments')

        comments = []
        for comment in complete_comment:
            comments.append({
                            'id': comment.get('id'),
                            'title': comment.get('title'),
                            'body': comment.get('body'),
                            'created_at': comment.get('created_at'),
                            'rate': comment.get('rate'),
                            'likes': comment.get('reactions').get('likes'),
                            'dislikes':comment.get('reactions').get('dislikes'),
                            'recommendation_status': comment.get('recommendation_status'),
                            'is_buyer': comment.get('is_buyer'),
                            'user_name': comment.get('user_name'),
                            'is_anonymous': comment.get('is_anonymous'),
                            })

        if pager:
            return  comments, data.get('pager')
        return comments
    return []


if __name__ == '__main__':
    product_id = 3493882
    sesstion = requests.Session()

    comments, pager = getComment(sesstion, product_id, pager=True)
    total_pages = pager.get('total_pages')

    for page in range(1, total_pages + 1):
        comment = getComment(sesstion, product_id, page=page)
        comments.extend(comment)
    sendCommentsIntoMongo(comments)
