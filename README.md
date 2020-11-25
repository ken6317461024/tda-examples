# TDA

This repository is a collection of python programs written from early 2020 to present on topological data analysis. The file structure is as follows: 

## Structure 

- __Complete__ contains "complete" programs. These should be stable and serve a well-defined purpose.
- __Auxilliary__ contains programs that are not directly related to TDA but are used in an integral way nonetheless. For instance, linear algebra functions that are used in homology computations. A future implementation of these TDA programs can be cleaned up significantly by importing these programs and calling the functions from them.
- __Tests__ contains programs which were used to run tests. In the future, tests will be run in a more "git" way, i.e. with branches. Therefore, tests is a relic of the pre-git life. 

## Going forward 

Specific future projects should be created in a new, fresh repository, taking from this one as needed. This repository is a record of work that was done to better understand how TDA works and get practice with building code that implemented it. Ultimately, implementing TDA to solve serious mathematical programs would be much more efficient utilizing existing python TDA packages, like giotta. 

