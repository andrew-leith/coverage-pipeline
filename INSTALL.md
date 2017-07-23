# Coverage Pipeline

A pipeline for computing coverage from fastq files using the BWA aligner.

## Installation

This software requires R to be installed on the system.  R can be obtained from CRAN (https://cran.r-project.org/) or through most Linux distro package managers.

Furthermore, two R packages are required to run the software.  One is the 'rmarkdown' package hosted on CRAN, while the other is the 'Biostrings' package available through Bioconductor.

Other dependencies can be efficiently installed through the Conda package manager.

	conda install bwa
	conda install samtools
	conda install bedtools
	conda install pandoc

Any other method of installation is fine as long as the resulting binaries are added to the user's PATH.  BWA, Samtools, and Bedtools are used for processing the sequence files, while pandoc is used to compile the pdf upon completion of the analysis.