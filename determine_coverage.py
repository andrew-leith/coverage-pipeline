import argparse
import os
import subprocess

parser = argparse.ArgumentParser(description='Align files, calculate coverage, print output to files.')
parser.add_argument('-1', '--read-1', type=str, required = True)
parser.add_argument('-2', '--read-2', type=str, required = True)
parser.add_argument('-x', '--reference-genome', type=str, required = True)
parser.add_argument('-q', '--quality-threshold', type=int, default = 0)
parser.add_argument('-i', '--index', default=False, action='store_true')
parser.add_argument('-t', '--aligner-threads', type=str, default = "1")
parser.add_argument('-d', '--delete-alignment', default=False, action='store_true')

results = parser.parse_args()

#if asked to index the reference genome, do so
if results.index == True:
	subprocess.call(['bwa index '+ results.reference_genome], shell=True)

#if quality threshold is above the designated range, set it to the upper boundary of the range
if results.quality_threshold > 41:
	results.quality_threshold = 41

#generate filenames, named based on the first fastq
base_filename = results.read_1.split('_')[0]
sam_filename = base_filename + ".sam"
bam_filename = base_filename + ".bam"


subprocess.call(['bwa mem -t '+ results.aligner_threads +' '+ results.reference_genome +' '+ results.read_1 +' '+ results.read_2 +'> '+ sam_filename], shell=True)
subprocess.call(['samtools view -@ '+ results.aligner_threads+' -bSq '+ str(results.quality_threshold) +' '+ sam_filename +' > '+ bam_filename], shell=True)
#flagstat goes here
subprocess.call(['bedtools genomecov -ibam '+ bam_filename +' -d > coverage.tsv'], shell=True)
subprocess.call(['Rscript coverage.R coverage.tsv '+ results.reference_genome], shell=True)

if results.delete_alignment == True:
		subprocess.call(['rm '+ sam_filename +' '+ bam_filename], shell=True)
