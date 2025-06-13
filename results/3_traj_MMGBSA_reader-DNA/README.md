# MM/GBSA of readers with nucleosomes

Folders contain results of MM/GBSA analyses on reader interactions with nucleosomes. Each folder has the output files from out runs and accompanying notebooks for sorting data into figures or numbers for tables.

If recreating our results, you will want to:

1) Sort the output .xvg files (time series of energy components) into appropriate folders

2) Run the "Prep_xvg_files.ipynb" notebook, editing the names of the input files as necessary. This will add '#' characters to the xvg files to make them easier to parse in the other notebook.

3) Run the "Evaluate_averages.ipynb" notebook, editing the names of the input and output files as necessary. This will combine appropriate values, calculate the statistical inefficiency, and print the final averages and errors.
