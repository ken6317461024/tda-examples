# TDA

This repository is a collection of python programs written from early 2020 to present on topological data analysis. The file structure is as follows: 

## Structure 

- __Old__ contains programs which appear, to the best of my ability, to be deprecated, including a combination of outdated tests and less efficient implementations of homology, vietoris rips, and persistence algorithms.
- __Tests__ contains programs which were used to run tests. In the future, tests will be run in a more "git" way, i.e. with branches. Therefore, tests is a relic of the pre-git life. 
- __Auxilliary__ contains programs that are not directly related to TDA but are used in an integral way nonetheless. For instance, linear algebra functions that are used in homology computations. A future implementation of these TDA programs can be cleaned up significantly by importing these programs and calling the functions from them.
- __Complete__ contains "complete" programs. These should be stable and serve a well-defined purpose.

## Going forward 

If this repository is used going forward, the "complete" programs should be cleaned up significantly. Functions should be allocated to separate python files and called in the main program. This will include the auxilliary programs, but it will also involve creating new python files, which in a sense "partition" some current ones. Doing this will make it much easier to track progress, understand dependencies, and simply read the code.  

Specific future projects should be created in a new, fresh repository, taking from this one as needed. This repository is a record of work that was done to better understand how TDA works and get practice with building code that implemented it. Ultimately, implementing TDA to solve serious mathematical programs would be much more efficient utilizing existing python TDA packages, like giotta. 

