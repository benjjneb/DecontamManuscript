# Reproducible Analyses from the Manuscript Introducing decontam

This repository hosts the reproducible workflow that performed the analyses presented in the manuscript ["Simple statistical identification and removal of contaminant sequences in marker-gene and metagenomics data" by Davis et al. Microbiome, 2018](https://doi.org/10.1186/s40168-018-0605-2).
Rmarkdown documents are hosted in the `Analyses/` directory. The input data is hosted in several subdirectoryies (e.g. `Analyses/LauderPlacenta`).
You can run these analyses on your own machine by (1) cloning the repository, (2) modifying the paths defined at the start of each Rmd document, (3) installing required libraries, and (4) pressing Run!

These Rmarkdown documents have also been rendered into html format, and can be viewed in your web browser:

* Classification of sequence variants by decontam [is consistent with expectations based on prior evidence in the human oral microbiome](https://benjjneb.github.io/DecontamManuscript/Analyses/oral_contamination.html).
* Removal of contaminants identified by decontam [dramaticaly reduces kit and sequence-center effecst in a dilution series experiment](https://benjjneb.github.io/DecontamManuscript/Analyses/salter_metagenomics.html).
* [decontam confirms the lack of evidence for a placenta microbiome in a 16S rRNA gene dataset](https://benjjneb.github.io/DecontamManuscript/Analyses/lauder_placenta.html), even amongst the rarest variants.
* decontam corroborated suspicions that [run-specific contaminants contributed to false-positives in exploratory analysis of associations between low-frequency taxa and preterm birth](https://benjjneb.github.io/DecontamManuscript/Analyses/callahan_ptb.html).

## Decontam

The decontam R package is available through GitHub and Bioconductor.

* decontam GitHub repository: https://github.com/benjjneb/decontam
* decontam Bioconductor page: https://www.bioconductor.org/packages/release/bioc/html/decontam.html
* decontam website: https://benjjneb.github.io/decontam/

The decontam R package is maintained by Benjamin Callahan (benjamin DOT j DOT callahan AT gmail DOT com). Twitter: [\@bejcal](https://twitter.com/bejcal)
