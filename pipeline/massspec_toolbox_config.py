import os

toolbox_home = '/home/taejoon/massspec-toolbox/'
path_formatdb = '/usr/bin/formatdb'
tandem_basedir = '/home/taejoon/MS.project/bin64/'
inspect_basedir = '/home/taejoon/MS.project/src64/inspect/'
crux_basedir = '/home/taejoon/MS.project/bin64/'
omssa_basedir = '/usr/local/src/omssa-2.1.4.linux/'

def get_dbinfo():
    f_dbinfo = open('DB/DBINFO','r')
    (db_name, filename_fasta) = f_dbinfo.readline().strip().split()
    f_dbinfo.close()
    return db_name, filename_fasta

def get_TPP_path(filename):
    TPP_basedir = '/usr/local/tpp/bin/'
    return os.path.join(TPP_basedir,filename)

def get_tandem_path(filename):
    if( filename == 'tandem-input' ):
        return os.path.join(toolbox_home,'config','tandem-isb_input_native.xml')
    elif( filename == 'tandem-input_k' ):
        return os.path.join(toolbox_home,'config','tandem-isb_input_kscore.xml')
    return os.path.join(tandem_basedir,filename)

def get_inspect_path(filename):
    return os.path.join(inspect_basedir,filename)

def get_crux_path(filename):
    return os.path.join(crux_basedir,filename)

## OMSSA
def get_omssa_path(filename):
    if( filename == 'omssa-mods' ):
        return os.path.join(toolbox_home,'config','omssa-mods.xml')
    elif( filename == 'formatdb' ):
        return path_formatdb
    return os.path.join(omssa_basedir,filename)

## APEX
def get_TPP2APEX_parser(filename):
    return os.path.join(toolbox_home,'APEX','np_parse_ProteinProphet.pl')
