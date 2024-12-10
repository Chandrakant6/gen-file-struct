# generate-file-structure
generate file structure from given text or md file
it only work on linux to run on windoes install wls

## what it does
when you want to build or start a project you need to set up a file structure for that project, It is not an easy task for large project therefore this project is build to automate that task to set up your project file structure.

you need to provide yiur file structur in text or markdown(.md) file like this :-

Text / Markdown file
```
root
  - sub1
    - sub1a
    - sub1b
  - sub2
  - sub3
```

## setup 
download repo
```
git clone https://github.com/Chandrakant6/generate-file-structure
```
make it executable
```
chmod +x gen-struct.sh
```
use it
```
gen-struct.sh <project-strut.txt> </path/to/root>
```
and all done
