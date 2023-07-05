import os

def sort_file(source_path, dest_path):
    global_content = []
    for file_ in os.listdir(source_path):
        #read the file for contents
        with open(source_path +file_, "r") as f:
            for line in  f.readlines():
                # print(line)
                line = line.strip()
                if not line: continue
                (t, u) = line.split(" ")
                # collect all the file contents
                global_content.append((int(t), u))
    # sort global content by key
    sorted_content = sorted(global_content, key=lambda x: x[0])
    with open(dest_path +"-".join(os.listdir(source_path)) +"-merged.log", "w+") as f:
        for tup in sorted_content:
            f.write(" ".join([str(i) for i in tup])+ "\n")

if __name__ == "__main__":
   sort_file(os.path.realpath(".")+"/files/", os.path.realpath(".")+"/files_p/")
