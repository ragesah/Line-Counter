import os


# helper functions
def count_lines(p):
    p = p.replace("\\","/")
    with open(p) as f:
        return len(f.readlines())

def folder_explorer(path, nfiles, nlines, fformat='txt'):
    fcomponets = path.split('.')
    
    # if file format matched, process
    if len(fcomponets) > 1 and fcomponets[-1] == fformat: 
        nfiles[0] += 1
        nlines[0] += count_lines(path)
        print(path,  "{}".format(count_lines(path)))
        return 
    
    # if file format NOT matched, return
    if len(fcomponets) > 1 and fcomponets[-1] != fformat:
        return
    
    for cf in os.listdir(path):
        # attach current folder
        path = os.path.join(path, cf)
        folder_explorer(path, nfiles, nlines, fformat)
        # detach current folder
        path = "\\".join(path.split("\\")[:-1])
    