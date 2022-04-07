## Main Process
- Step1, split gVCF files into regions
  - Tool: [gvcf_splitter](https://cavatica.sbgenomics.com/u/yuankun/gmkf-cohort-joint-genotyping-method/apps/#yuankun/gmkf-cohort-joint-genotyping-method/gvcf_splitter)
  - Splitting intervals: [gvcf_splitting_intervals.bed](https://gist.github.com/yuankunzhu/e6d77c415c0fca78e778ac2b8f4a11c6)

- Step2, Joing Genotyping on each region
  - Tool: [gatk4-genotypegvcfs-wf](https://cavatica.sbgenomics.com/u/yuankun/gmkf-cohort-joint-genotyping-method/apps/#yuankun/gmkf-cohort-joint-genotyping-method/gatk4-genotypegvcfs-wf)

- Step3, Merge and VQSR 
  - Tool: [kfdrc-jointgenotyping-merge-recalibrate](https://cavatica.sbgenomics.com/u/yuankun/gmkf-cohort-joint-genotyping-method/apps/#yuankun/gmkf-cohort-joint-genotyping-method/kfdrc-jointgenotyping-intervals)
  - References/Known Sites:
    - axiomPoly_resource_vcf: [Axiom_Exome_Plus.genotypes.all_populations.poly.hg38.vcf.gz](https://cavatica.sbgenomics.com/u/yuankun/gmkf-cohort-joint-genotyping-method/files/624f0e5eddb7194afe396149/)
    - dbsnp_vcf: [Homo_sapiens_assembly38.dbsnp138.vcf](https://cavatica.sbgenomics.com/u/yuankun/gmkf-cohort-joint-genotyping-method/files/624f0e5eddb7194afe396148/)
    - hapmap_resource_vcf: [hapmap_3.3.hg38.vcf.gz](https://cavatica.sbgenomics.com/u/yuankun/gmkf-cohort-joint-genotyping-method/files/624f0e5eddb7194afe396146/)
    - mills_resource_vcf: [Mills_and_1000G_gold_standard.indels.hg38.vcf.gz](https://cavatica.sbgenomics.com/u/yuankun/gmkf-cohort-joint-genotyping-method/files/624f0e5eddb7194afe396147/)
    - omni_resource_vcf: [1000G_omni2.5.hg38.vcf.gz](https://cavatica.sbgenomics.com/u/yuankun/gmkf-cohort-joint-genotyping-method/files/624f0e5eddb7194afe396145/)
    - one_thousand_genomes_resource_vcf: [1000G_phase1.snps.high_confidence.hg38.vcf.gz](https://cavatica.sbgenomics.com/u/yuankun/gmkf-cohort-joint-genotyping-method/files/624f0e5eddb7194afe396144/)
    - reference_dict: [Homo_sapiens_assembly38.dict](https://cavatica.sbgenomics.com/u/yuankun/gmkf-cohort-joint-genotyping-method/files/624f0e5eddb7194afe39614a/)
    - wgs_evaluation_interval_list: [wgs_evaluation_regions.hg38.interval_list](https://cavatica.sbgenomics.com/u/yuankun/gmkf-cohort-joint-genotyping-method/files/624f0e5eddb7194afe396143/)

Step4 (Optional), Genotype Refinement & Posterior Probabilities

## Cavatica API Usage
```bash
$ pip install sevenbridges-python
```

```python
import sevenbridges as sbg
api = sbg.Api(url='https://cavatica-api.sbgenomics.com/v2', token='<TOKEN_HERE>')
```

### Step1, split gVCF files into regions
Because of the large number of files, we suggest to split them into multiple projects while they are created

- Create a new project
```python
api.projects.create(name="My new project", billing_group='296a98a9-424c-43f3-aec5-306e0e41c799')
```

- Run task
```python
Single task
# Task name
name = 'my-first-task'

# Project in which I want to run a task.
project = 'my-username/my-project'

# App I want to use to run a task
app = 'my-username/my-project/my-app'

# Inputs
inputs = {}
inputs['FastQC-Reads'] = api.files.query(project='my-project', metadata={'sample': 'some-sample'})

try:
    task = api.tasks.create(name=name, project=project, app=app, inputs=inputs, run=True)
except SbError:
    print('I was unable to run the task.')

# Task can also be ran by invoking .run() method on the draft task.
task.run()
```

- Task Status
```python
task.status
```