ICCM TransSet
=============

Companion repository for the 2019 article "" published for the 17th Annual Meeting of the International Conference on Cognitive Modelling.

## Overview

- `mfa-analysis/`: Scripts for the MFA agreement analysis (Figure 2)
    - `mfa-analysis/mfa_tables/`: MFA response tables extracted from Khemlani & Johnson-Laird (2012) and [Ragni2016](https://github.com/CognitiveComputationLab/ccobra/blob/master/benchmarks/syllogistic/data/Ragni2016.csv)
    - `mfa-analysis/models/`: Model prediction tables (non-transset models extracted from Khemlani & Johnson-Laird, 2012)
    - `mfa-analysis/mfa_agreement.py`: Plotting script
- `swarmplot/`: Scripts for the individualized analysis (Figure 3)
    - `swarmplot/ccobra_eval/`: CCOBRA benchmarking files for the individualized analysis
    - `swarmplot/create_swarmplot.py`: Plotting script

## Dependencies

- Python 3
    - [CCOBRA v0.0.14](https://github.com/CognitiveComputationLab/ccobra)
    - [pandas](https://pandas.pydata.org)
    - [numpy](https://www.numpy.org)
    - [seaborn](https://seaborn.pydata.org)

## Quickstart

### MFA Agreement Analysis (Figure 2)

Navigate into the `analysis/mfa-analysis/` folder and execute the plotting script:

```
$> cd /path/to/repository/analysis/mfa-analysis/
$> python mfa_agreement.py
```

### Individual Analysis (Figure 3)

Navigate into the `analysis/swarmplot/` folder and execute the plotting script:

```
$> cd /path/to/repository/analysis/swarmplot/
$> python create_swarmplot.py
```

The swarm plot requires a CCOBRA result table (located in `.../analysis/swarmplot/ccobra_eval/results.csv`). This file can be reproduced by executing the provided CCOBRA benchmark (`.../analysis/warmplot/ccobra_eval/bench.json`):

```
$> cd /path/to/repository/analysis/swarmplot/ccobra_eval/
$> ccobra bench.json -s results.csv
```

**Note**: This requires the CCOBRA framework to be installed on your system. See [CCOBRA repository](https://github.com/CognitiveComputationLab/ccobra) for instructions.

## Reference

Brand, D., Riesterer, N., & Ragni, M. (2019). On the Matter of Aggregate Models for Syllogistic Reasoning: A Transitive Set-Based Account for Predicting the Population. In Stewart T. (Ed.), Proceedings of the 17th International Conference on Cognitive Modeling.
