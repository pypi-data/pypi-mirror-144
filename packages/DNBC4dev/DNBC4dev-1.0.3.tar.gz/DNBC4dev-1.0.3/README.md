# DNBC4tools
An open source and flexible pipeline to analysis high-throughput DNBelab C Series single-cell RNA datasets
## Introduction
- **Propose**
  - An open source and flexible pipeline to analyze DNBelab C Series<sup>TM</sup> single-cell RNA datasets. 
- **Language**
  - Python3 and R scripts.
- **Hardware/Software requirements** 
  - x86-64 compatible processors.
  - require at least 50GB of RAM and 4 CPU. 
  - centos 7.x 64-bit operating system (Linux kernel 3.10.0, compatible with higher software and hardware configuration). 

## Installation
installation manual

### Install miniconda and creat DNBC4tools environment
- Creat DNBC4tools environment
```
cd DNBC4tools
source /miniconda3/bin/activate
conda env create -f DNBC4tools.yaml -n DNBC4tools
```
- Install R package that cannot be installed using conda
```
conda activate DNBC4tools
Rscript -e "devtools::install_github(c('chris-mcginnis-ucsf/DoubletFinder','ggjlab/scHCL','ggjlab/scMCA'),force = TRUE);"
```