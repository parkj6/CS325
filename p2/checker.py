import os.path
import sys, getopt

def gen_matrix(sizex, sizey):
    return [[0]*sizey for i in xrange(sizex)]

class ScoreParam:
    def __init__(self, loss_matrix, x_indexdict, y_indexdict):
        self.loss_matrix = loss_matrix
        self.x_indexdict = x_indexdict
        self.y_indexdict = y_indexdict
        
    def loss_char(self, xc , yc):
        return self.loss_matrix[self.x_indexdict[xc] ][ self.y_indexdict[yc] ]

def check_file(f_pth):
    if not os.path.exists(f_pth):
        p = 'no file: %s'% f_pth
        print(p)
        raise 'file not found'

def read_cost_matrix(fns=''):
    loss_matrix = []
    x_indexdict = {}
    y_indexdict = {}
    check_file(fns)

    with open(fns, 'r') as f:
        i = 0
        l = f.readline()
        while (l):
            if i == 0:
                ys = [y.strip() for y in l.split(',')[1:] ]
            if i > 0:
                x = l.split(',')[0].strip()
                x_indexdict [x] = i - 1
                r = []
                for j, s in enumerate(l.split(',') ):
                    if j > 0:
                        y_indexdict[ ys[ j - 1 ] ] = j - 1
                        r.append( int(s) )
                loss_matrix.append(r)
            i += 1
            l = f.readline()

    return loss_matrix, x_indexdict, y_indexdict

def get_cost(ax, ay, loss_matrix, x_indexdict, y_indexdict):
    cost = 0
    for i, ai in enumerate(ax):
        cost += loss_matrix[x_indexdict[ ai ] ][  y_indexdict[ ay[i] ]  ]
    return cost

def verifier(fnx='', fny='', fno=''):
    ##print('verifier ...')
    fails = 0
    check_file(fnx)
    check_file(fny)

    with open(fnx, 'r') as fix:
        with open(fny, 'r') as fiy:
            with open(fno, 'w') as fw:
                lx, ly = fix.readline(), fiy.readline()
                while(lx and ly):
                    lx = lx.strip()
                    ly = ly.strip()
                    lxs = lx.split(':')
                    lys = ly.split(':')
                    if len(lxs ) != 2 or len(lys)!= 2:
                        raise 'files should have tagged costs; use coster first'
                    if lxs[-1] == lys[-1]:
                        fw.write('Passed' + '\n')
                    else:
                        fails += 1
                        fw.write('%s: seq1: %s | seq2:%s \n'% ('Failed', lx, ly ) )
                         
                    
                    lx, ly = fix.readline(), fiy.readline()
                
                if (lx or ly):
                    raise 'the number of lines in the files are not equal'

    ###print('finished verifier: verify output at %s' % fno )
    ###print('failures: %s' % str(fails))
    return fails


def coster(fni='', fno='', loss_matrix=None, x_indexdict=None, y_indexdict=None):
    ##print('coster ... ')
    check_file(fni)

    with open(fni, 'r') as fi:
        with open(fno, 'w') as fw:
            l = fi.readline()
            while(l):
                axy_s = l.split(':')
                ax, ay = axy_s[0].split(',')
                if len(ax) != len(ay):
                    raise 'Ivalid alignments: the length of two alignments should be equal'
                c = get_cost(ax,ay, loss_matrix, x_indexdict, y_indexdict)
                fw.write(ax + ',' + ay + ':' + str(c) + '\n')
                l = fi.readline()
    ###print('finished coster: cost file saved at %s'%( fno ))


def main(argv):
    print('_'*100)

    inputfile =  ''
    outputfile = ''
    costfile = ''
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    """
    try:
        opts, args = getopt.getopt(argv,"hi:c:o:",["ifile=","cfile=", "ofile="])
    except getopt.GetoptError:
        print 'coster.py -i <inputfile> -c <costfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -c <costfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg.split(  )
        elif opt in ("-c", "--cfile"):
            costfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if inputfile == '' and outputfile == '':
        print('python checker.py' )
        print('example:python checker.py')
        sys.exit()
    """

    loss_matrix, x_indexdict, y_indexdict = read_cost_matrix( fns ='imp2cost.txt' )
    coster(fni='imp2output.txt', fno='imp2out_tagged.txt', loss_matrix=loss_matrix, x_indexdict=x_indexdict, y_indexdict=y_indexdict)
    step1_fails = verifier(fnx='imp2output.txt', fny='imp2out_tagged.txt', fno='imp2out_fails_1.txt')
    print('Step %s ... %s'%('1', 'check whether DP\'s output match the cost of the alignments'))
    if step1_fails > 0:
        print("Failurs (Step %s): %s" % ('1', str(step1_fails)) )
        print("Please find more info at %s"% ('imp2out_fails_1.txt'))
        sys.exit()
    else:
        print("Passed Successfully")
    """
    else:
        print('Passed Step 1')
        print('Step %s ... %s'%('2', 'check whether DP\'s output match our provided output for the given input'))
        step2_fails = verifier(fnx='imp2out_tagged.txt', fny='imp2output_our.txt', fno='imp2out_fails_2.txt')
        if step2_fails == 0:
            print('Passed Successfully')
        else:
            print("Failurs (Step %s): %s" % ('2', str(step2_fails)) )
            print("Please find more info at %s"% ('imp2out_fails_2.txt'))
            sys.exit()
    """
   

if __name__ == "__main__":
    main(sys.argv[1:])


