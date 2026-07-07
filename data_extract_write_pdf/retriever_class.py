import xlwings as xw                            
import pdfplumber
import re
from datetime  import datetime,date 
import os
import pandas as pd

class Retriever:     
  def __init__(self,keys:list,values:list):
    self.keys=keys
    self.values=values
    
  def create_dictionary(self,keys:list,values:list):
    self.dictionary={k:v for (k,v) in zip(keys,values)}
    return self.dictionary
  
  def create_dataframe(self,keys,values): 
    self.dic_to_dataframe=pd.DataFrame(self.create_dictionary(keys,values))
    return self.dic_to_dataframe
  
  def join_dataframes(self,first_dataframe,second_dataframe):
    self.dataframe = pd.concat([first_dataframe,second_dataframe], axis=0)
    return self.dataframe
  
  def folder_files(self,completefolderpath):
    """
    Retrieve a list of all files and directories within a specified folder.

    Args:
        completefolderpath (str): The full path to the target directory.

    Returns:
        list: A list containing the names of files and subdirectories
              in the given folder..
    """
    #self.path=(r"completepath")
    self.all_files=os.listdir(completefolderpath)
    return self.all_files
  
  def files_series(self,completefolderpath,series1,series2,series3):
    files=os.listdir(completefolderpath)
    self.series_list=[]
    for file in files:
      if (file.startswith(series1)) or (file.startswith(series2)) or (file.startswith(series3)):      
        #full_path = os.path.join(completefolderpath, file)
        self.series_list.append(file)
    return self.series_list
  def inward_data(self,file,completefolderpath):
    if file.lower().endswith(".pdf"):     #converts all letters in file name into lowercase and check if ends with pdf (to handle both pdf and PDF)
      file_full_path = os.path.join(completefolderpath, file)
      with pdfplumber.open(file_full_path) as pdf:
    
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
        inward = re.findall(r"RECEIVED BY YOU.*?(.*?)DELIVERED BY YOU", text,re.DOTALL)
        inward = ' '.join(inward)
        branch_code_inw = re.findall(r"^\d{4}\s", inward,re.MULTILINE)
        branch_name_inw = re.findall(r"\d{4}\s+(.*?)\s+GROUP", inward,re.MULTILINE) 
        item_count_inw = re.findall(r"GROUP B\s*[:=]\s*(\d{1,2})\s",inward,re.MULTILINE)
        total_amount_inw = re.findall(r"GROUP B\s*[:=]\s\d{1,2}\s*([\d,.]+)", inward,re.MULTILINE)
        clearing_type_inw=["RECEIVED BY YOU"  for i in range(len(branch_code_inw)) ]
        keys=['branch_code','branch_name','item_count','total_amount','clearing_type']
        values_inw=[branch_code_inw,branch_name_inw,item_count_inw,total_amount_inw,clearing_type_inw]
        self.df_inw=self.create_dataframe(keys,values_inw)
    return  self.df_inw
  def outward_data(self,file,completefolderpath):
    if file.lower().endswith(".pdf"):     #converts all letters in file name into lowercase and check if ends with pdf (to handle both pdf and PDF)
      file_full_path = os.path.join(completefolderpath, file)
    
      with pdfplumber.open(file_full_path) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
        outward = re.findall(r"DELIVERED BY YOU.*?(.*?)SUMMARY", text,re.DOTALL)
        outward = ' '.join(outward)

        branch_code_outw = re.findall(r"^\d{4}\s", outward,re.MULTILINE)
        branch_name_outw = re.findall(r"\d{4}\s+(.*?)\s+GROUP", outward,re.MULTILINE)
        item_count_outw = re.findall(r"GROUP B\s*[:=]\s*(\d{1,2})\s",outward,re.MULTILINE)
        total_amount_outw = re.findall(r"GROUP B\s*[:=]\s\d{1,2}\s*([\d,.]+)", outward,re.MULTILINE)
        clearing_type_outw=["DELIVERED BY YOU"   for i in range(len(branch_code_outw))]
        keys=['branch_code','branch_name','item_count','total_amount','clearing_type']
        values_outw=[branch_code_outw,branch_name_outw,item_count_outw,total_amount_outw,clearing_type_outw]
        self.df_outw=self.create_dataframe(keys, values_outw)
    return  self.df_outw
  def date_extraction(self,file,completefolderpath):
    if file.lower().endswith(".pdf"):     #converts all letters in file name into lowercase and check if ends with pdf (to handle both pdf and PDF)
       file_full_path = os.path.join(completefolderpath, file)
    
       with pdfplumber.open(file_full_path) as pdf:
    
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
        date_match=re.findall(r"CLEARING AS ON\s*(\d{2}-\d{2}-\d{4})",text,re.MULTILINE)
        self.valid_date=None                           #validating date as real date
        if date_match!=[]:
          self.valid_date = datetime.strptime(date_match[0], '%d-%m-%Y').date()
        else:
          pass
    return self.valid_date
    
