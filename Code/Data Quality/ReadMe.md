1- Create a data context
Command : great_expectations init

2- Create a new data source
Command : great_expectations datasource new

Options:
A- Select files on filesystem
B- Select Pandas
C- Enter file's directory

3- When Jupyter notebook open type the datasource name that you want in corresponding cell and run all cells
then shutdown jupyter

4- Create expectation suite
command: great_expectations suite new

Options:
A- select third item
B- select the file that you want to be base as data asset
C- Choice name for suite
D- Accept the settings

After all a jupyter notebook will be open. In "exclude_column_names" cell comment or delete lines that 
you want to involving in processing and then run all cells. after all step shutdown jupyter notebook

5- Validate data
Command: great_expectations checkpoint new getting_started_checkpoint

This command will open a jupyter notebook. in the cell that start with "yaml_config" set your file that want to be validate.
Then run all cells

