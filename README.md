# caqe_segmentation

This is the experiment and plotting code repository for the (in review) paper, 
''Re-visiting the Music Segmentation Problem with Crowdsourcing'', submitted to ISMIR2017.

## The AMT-pilot dataset
The annotaions gathered in this work by Cheng-i Wang should be referred to as the ''AMT-pilot'' database. This dataset contains AMT annotations on 8 songs from Beatles-TUT and SALAMI. 

## Error Corrections

1. Figure 2(b) should be ''Out in the Cold'' from Carole King instead of ''Black or White'' from Michael Jackson.
2. In Table 3, 4 and 5, ''Out in the Cold'' and ''Black or White'' are misplaced with each other.
3. The titles for Figure 3(b) and Figure 3(b) are misplaced between ''Out in the Cold'' and ''Black or White''. 

## Code Summaries

### caqe_boundary python module
A flask-sqlalchemy setup that builds databases specifically for analyzing annotation data.

### Jupyter Notebooks
* beatles_db_extract.ipynb and salami_db_extract.ipynb extract AMT annotations from beatles_accpted.csv and salami_accepted.csv 
and build SQL databases.
* beatles_stats.ipynb and salami_stats.ipynb plot graphs and calculate statistics used in the submitted paper.

### CSV Files
beatles_accpted.csv and salami_accepted.csv contain the extracted accepted annotations from AMT 
using the CAQE extension developped for this paper

### Audio Folders
Contain original song files, chopped 20-seconds clips and randomized 10-clip tasks.

### Misc
.dump files are the databases for the entire AMT tasks. 
Utility jupyter notebooks in mturk_utils folder are used to chopping songs and assigning chopped clips to tasks.  
