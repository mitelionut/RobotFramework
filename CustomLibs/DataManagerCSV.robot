*** Settings ***
Documentation     Use this for CSV Files
Library           csv.py

*** Keywords ***
Get CSV Data
    [Argumets] ${FilePath}
    ${Data} = read csv file ${FilePath}
    [Return] ${Data}