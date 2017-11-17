#concatenate hypo1a and hypo1b
mkdir hypo_sa1_0001
cat Relman_Hypo1a_NoIndex_L001_R1_001.fastq Relman_Hypo1b_NoIndex_L001_R1_001.fastq > hypo_sa1_0001/fwd.fastq
cat Relman_Hypo1a_NoIndex_L001_R2_001.fastq Relman_Hypo1b_NoIndex_L001_R2_001.fastq > hypo_sa1_0001/index.fastq
cat Relman_Hypo1a_NoIndex_L001_R3_001.fastq Relman_Hypo1b_NoIndex_L001_R3_001.fastq > hypo_sa1_0001/rev.fastq
cd hypo_sa1_0001

#demultiplex (split libraries), setting all quality parameters to lowest thresholds, effectively eliminating the quality filtering step.
split_libraries_fastq.py -i fwd.fastq -m hypo_sa1_0001_mappingfile.txt -b index.fastq -q 0 -n 200 -r 200 -p 0 -o f/ --store_demultiplexed_fastq --rev_comp_barcode --rev_comp_mapping_barcodes
split_libraries_fastq.py -i rev.fastq -m hypo_sa1_0001_mappingfile.txt -b index.fastq -q 0 -n 200 -r 200 -p 0 -o r/ --store_demultiplexed_fastq --rev_comp_barcode --rev_comp_mapping_barcodes

#check for same length
cd ..
wc -l hypo_sa1_0001/f/seqs.fastq
wc -l hypo_sa1_0001/r/seqs.fastq

#split demultiplexed files on sequence ids
cd hypo_sa1_0001
split_sequence_file_on_sample_ids.py -i f/seqs.fastq --file_type fastq -o f/splitf/
split_sequence_file_on_sample_ids.py -i r/seqs.fastq --file_type fastq -o r/splitr/

##### rename files with "R1" and "R2" tags within directory. optionally add 'echo' between 'do' and 'mv' to pre-test
cd f/splitf/
for file in *.fastq; do mv $file `basename $file .fastq`_R1.fastq; done;
cd ..
cd ..
cd r/splitr/
for file in *.fastq; do mv $file `basename $file .fastq`_R2.fastq; done;

#these are ready for use with DADA2
