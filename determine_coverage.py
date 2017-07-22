import argparse
import os
import subprocess

parser = argparse.ArgumentParser(description='Align files, calculate coverage, print output to files.')
parser.add_argument('-1', '--read-1', type=str, required = True)
parser.add_argument('-2', '--read-2', type=str, required = True)
parser.add_argument('-x', '--reference-genome', type=str, required = True)
parser.add_argument('-q', '--quality-threshold', type=str, default = "0")
parser.add_argument('-i', '--index', default=False, action='store_true')
parser.add_argument('-t', '--aligner-threads', type=str, default = 1)
#parser.add_argument('-c', '--check-quality', action='store_true', help="run FastQC on samples?")


results = parser.parse_args()
print results.read_1
print results.read_2
print results.reference_genome
print results.quality_threshold
print results.index

#if asked to index the reference genome, do so
if results.index == True:
	subprocess.call(['bwa index '+ results.reference_genome], shell=True)

#use read 1 to come up with the base name of the files
#use that variable to name the sam file and then the bam file
subprocess.call(['bwa mem -t '+ results.aligner_threads+' '+ results.reference_genome +' '+ results.read_1 +' '+ results.read_2 +'> SRR961514.sam'], shell=True)
subprocess.call(['samtools view -@ '+results.aligner_threads+' -bSq '+ results.quality_threshold +' SRR961514.sam > SRR961514.bam'], shell=True)
#flagstat goes here
#use the same bam file name from above
subprocess.call(['bedtools genomecov -ibam SRR961514.bam -d > coverage.tsv'], shell=True)
subprocess.call(['Rscript coverage.R coverage.tsv '+ results.reference_genome], shell=True)
#distribution of coverage for each base type
#K-S test to compare these distributions for any significant differences

