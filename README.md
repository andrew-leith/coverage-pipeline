# Coverage Pipeline

A description of the available arguments and an example of how to run the software.

## Arguments

	('-1', '--read-1')

This mandatory argument is used to denote the first fastq file

	('-2', '--read-2')

This mandatory argument is used to denote the second fastq file

	('-x', '--reference-genome')

This mandatory argument is used to denote the reference genome

	('-q', '--quality-threshold')

This argument is used to denote the read quality threshold.  Reads below that quality score will be discarded.  The default value is 0, but values up to 41 can be specified.  Larger values will be thresholded at 41.

	('-i', '--index')

This optional argument tells BWA to index the reference genome before attempting alignment

	('-t', '--aligner-threads')

This argument specifies the number of threads to use for alignment and read processing.  The default value is 1.

	('-d', '--delete-alignment')

This optional argument tells the pipeline to discard the bam and sam files generated during alignment to save space on the user's system.

## Example

	python determine_coverage.py -1 SRR961514_1.fastq -2 SRR961514_2.fastq -x hiv_reference.fasta -t 8 -q 10 -d

This instantiation of the pipeline uses 8 threads to align SRR961514_1.fastq and SRR961514_2.fastq to hiv_reference.fasta.  It then discards reads with MAPQ less than 10, performs its analysis, and then removes the generated sam and bam files.  This command assumes the BWA index for hiv_reference.fasta already exists.