# Nextflow Pipeline Request Guide

This guide explains what you need to prepare before submitting a pipeline request. Please read the relevant section for your pipeline, then [submit your request](https://forms.cloud.microsoft/e/P5guQdhnjR).

## Before you request

For all pipelines, you will need:

- **Data on RDSS** — your input files must be on RDSS with a known path
- **An RDSS location for results** — confirm where you want outputs delivered
- **A samplesheet** — a CSV file describing your samples (format varies by pipeline — see below)
- **A genome reference** — either a standard [iGenomes](https://nf-co.re/docs/usage/reference_genomes) name (e.g. `GRCh38`, `GRCm39`) or, for non-model organisms, the path to your own genome FASTA and annotation (GTF/GFF) files on RDSS
- **Familiarity with the pipeline** — you must read the pipeline documentation and confirm you understand the standard outputs

If you need non-default parameters, note them in your request.

---

## nf-core/rnaseq

**Documentation:** [nf-co.re/rnaseq](https://nf-co.re/rnaseq)

**What it does:** Quality control, trimming, alignment, and quantification of bulk RNA-seq data.

**Samplesheet format:**

```csv
sample,fastq_1,fastq_2,strandedness
CONTROL_REP1,/path/to/S1_R1.fastq.gz,/path/to/S1_R2.fastq.gz,auto
CONTROL_REP2,/path/to/S2_R1.fastq.gz,/path/to/S2_R2.fastq.gz,auto
TREATMENT_REP1,/path/to/S3_R1.fastq.gz,/path/to/S3_R2.fastq.gz,auto
```

**What you need to specify:**
- Genome reference (e.g. `GRCh38`)
- Strandedness — use `auto` unless you know otherwise (options: `auto`, `forward`, `reverse`, `unstranded`)

**Defaults (unless you request otherwise):**
- Aligner: STAR + Salmon
- Trimmer: Trim Galore

---

## nf-core/sarek

**Documentation:** [nf-co.re/sarek](https://nf-co.re/sarek)

**What it does:** Germline and/or somatic variant calling from whole genome, whole exome, or targeted sequencing data.

**Samplesheet format (germline):**

```csv
patient,sample,lane,fastq_1,fastq_2
patient1,normal_sample,lane_1,/path/to/R1.fastq.gz,/path/to/R2.fastq.gz
```

**Samplesheet format (tumour-normal pair):**

```csv
patient,sex,status,sample,lane,fastq_1,fastq_2
patient1,XX,0,normal_sample,lane_1,/path/to/normal_R1.fastq.gz,/path/to/normal_R2.fastq.gz
patient1,XX,1,tumour_sample,lane_1,/path/to/tumour_R1.fastq.gz,/path/to/tumour_R2.fastq.gz
```

**What you need to specify:**
- Genome reference (e.g. `GATK.GRCh38`, path to your genome)
- Analysis type: germline only, or tumour-normal pair
- Variant calling tools (e.g. `HaplotypeCaller`, `Mutect2`, `Strelka`)
- Data type: WGS, WES, or targeted panel (provide BED file if targeted)
- Sex of patient (if tumour-normal, used for CNV calling)

**Defaults (unless you request otherwise):**
- Aligner: BWA-MEM
- Starting step: mapping
- Variant caller: gatk HaplotypeCaller

---

## nf-core/methylseq

**Documentation:** [nf-co.re/methylseq](https://nf-co.re/methylseq)

**What it does:** Alignment and methylation calling from bisulfite or TAPS sequencing data.

**Samplesheet format:**

```csv
sample,fastq_1,fastq_2,genome
SAMPLE1,/path/to/S1_R1.fastq.gz,/path/to/S1_R2.fastq.gz,
SAMPLE2,/path/to/S2_R1.fastq.gz,/path/to/S2_R2.fastq.gz,
```

**What you need to specify:**
- Genome reference (e.g. `GRCh38`, path to your genome)
- Protocol: bisulfite or TAPS
- Targeted sequencing? If yes, provide a BED file

**Defaults (unless you request otherwise):**
- Aligner: Bismark (Bowtie2)
- Trimmer: Trim Galore
- Protocol: bisulfite

---

## Requesting a new pipeline

If you need a pipeline not listed above, [fill in the new pipeline request form](https://forms.cloud.microsoft/e/i1wZabqP1i). We'll assess feasibility and add it to our roadmap where possible.
