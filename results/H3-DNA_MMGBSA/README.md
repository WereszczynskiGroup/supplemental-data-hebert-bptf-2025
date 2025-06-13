# MM/GBSA of H3 tails with DNA

Folders contain results of MM/GBSA analyses on H3 tail interactions with DNA. Each folder has the output files from our runs and accompanying notebooks for sorting data into figures or numbers for tables.

If recreating our results, you will want to:

1) Sort the output .xvg files (time series of energy components) into appropriate folders

2) Run the "Prep_xvg_files.ipynb" notebook, editing the names of the input files as necessary. This will add '#' characters to the xvg files to make them easier to parse in the other notebook.

3) Run the "[system]_averages.ipynb" notebooks, editing the names of the input and output files as necessary. This will combine appropriate values, calculate the statistical inefficiency, and print the final averages and errors.
