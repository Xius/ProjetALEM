def read(filename):
    opened = open(filename,'r')
    raw = opened.readlines()

    opened.close()
    dblast = {}
    print len(raw)
    for x in xrange(len(raw)):
        dblast[x] = raw[x].split('\t')
    return dblast

matA = read('BIOGRID-ORGANISM-Rattus_norvegicus-3.2.120.tab2.txt')
print len(matA)
print len(matA)