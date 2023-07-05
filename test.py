import os

def sort_file(dir_path):
    global_content = []
    for file_ in os.listdir(dir_path):
        #read the file for contents
        with open(dir_path +file_, 'r') as f:
            for line in  f.readlines():
                # print(line)
                line = line.strip()
                if not line: continue
                (t, u) = line.split(' ')
                # collect all the file contents
                global_content.append((int(t), u))
    # sort global content by key
    return sorted(global_content, key=lambda x: x[0])


if __name__ == '__main__':
   print(sort_file(os.path.realpath('.')+'/files/'))
