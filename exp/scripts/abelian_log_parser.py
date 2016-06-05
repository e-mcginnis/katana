import re
import sys, getopt
import csv

#CommandLine : /work/02982/ggill0/Distributed_latest/build_dist_hetero/release_new_gcc/exp/apps/hsssp/bfs_gen /work/02982/ggill0/Distributed_latest/inputs/pagerank/Galois/scalefree/NEW/rmat16-2e25-a=0.57-b=0.19-c=0.19-d=.05.gr -maxIterations=10000 -srcNodeId=0 -verify=0 -t=15

#Hostname : c453-401.stampede.tacc.utexas.edu

#Threads : 15

#Hosts : 32

#Runs : 3

#[31]STATTYPE,LOOP,CATEGORY,n,sum,T0,T1,T2,T3,T4,T5,T6,T7,T8,T9,T10,T11,T12,T13,T14
#[31]STAT,(NULL),RecvBytes,15,402945176,402945176,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),RecvNum,15,2480,2480,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PULL_BFS_0_1,15,4614,4614,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PULL_BFS_0_2,15,4629,4629,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PULL_BFS_0_3,15,4616,4616,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PULL_BFS_0_4,15,4619,4619,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PULL_BFS_1_1,15,4623,4623,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PULL_BFS_1_2,15,4617,4617,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PULL_BFS_1_3,15,4612,4612,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PULL_BFS_1_4,15,4624,4624,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PULL_BFS_2_1,15,4625,4625,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PULL_BFS_2_2,15,4633,4633,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PULL_BFS_2_3,15,4631,4631,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PULL_BFS_2_4,15,4626,4626,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PULL_InitializeGraph_0_1,15,160818,160818,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PULL_InitializeGraph_1_1,15,4656,4656,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PUSH_BFS_0_1,15,10967,10967,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PUSH_BFS_0_2,15,9759,9759,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PUSH_BFS_0_3,15,9766,9766,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PUSH_BFS_0_4,15,9763,9763,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PUSH_BFS_1_1,15,10953,10953,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PUSH_BFS_1_2,15,9774,9774,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PUSH_BFS_1_3,15,9760,9760,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PUSH_BFS_1_4,15,9772,9772,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PUSH_BFS_2_1,15,10956,10956,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PUSH_BFS_2_2,15,9762,9762,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PUSH_BFS_2_3,15,9756,9756,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SYNC_PUSH_BFS_2_4,15,9755,9755,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SendBytes,15,223858996,223858996,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),SendNum,15,2108,2108,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),TIMER_0,15,58743,58743,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),TIMER_1,15,58745,58745,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),TIMER_2,15,58751,58751,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),TIMER_GRAPH_INIT,15,156169,156169,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),TIMER_HG_INIT,15,17422,17422,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[31]STAT,(NULL),TIMER_TOTAL,15,359146,359146,0,0,0,0,0,0,0,0,0,0,0,0,0,0

#[13]STAT,PageRank,Commits,15,6377945,277895,324235,482281,296898,572496,295661,311751,434026,421630,445072,711824,444553,408666,535821,415136
#[13]STAT,PageRank,Conflicts,15,3167,196,281,296,210,438,288,203,304,135,128,213,111,106,152,106
#[13]STAT,PageRank,Iterations,15,6381112,278091,324516,482577,297108,572934,295949,311954,434330,421765,445200,712037,444664,408772,535973,415242
#[13]STAT,PageRank,Pushes,15,26999,3263,1940,2700,3747,2227,1977,2536,2264,694,895,720,1220,864,1006,946

def match_timers(fileName, benchmark, forHost, numRuns, numThreads):

  mean_timer = 0.0;
  recvNum_total = 0
  recvBytes_total = 0
  sendNum_total = 0
  sendBytes_total = 0
  sync_pull_avg_time_total = 0.0;
  sync_push_avg_time_total = 0.0;
  graph_init_time = 0
  hg_init_time = 0
  total_time = 0


#[15]STAT,(NULL),SYNC_PUSH_PageRank_2_95,15,1559,1559,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[15]STAT,(NULL),SYNC_PUSH_PageRank_2_96,15,1560,1560,0,0,0,0,0,0,0,0,0,0,0,0,0,0
#[15]STAT,(NULL),SYNC_PUSH_PageRank_2_97,15,1559,1559,0,0,0,0,0,0,0,0,0,0,0,0,0,0

  timer_regex = re.compile(r'\[' + re.escape(forHost) + r'\]STAT,\(NULL\),TIMER_(\d*),' + re.escape(numThreads) + r',(\d*),(\d*).*')

  log_data = open(fileName).read()

  timers = re.findall(timer_regex, log_data)
  print timers

  for timer in timers:
    mean_timer = mean_timer + float(timer[2])

  mean_timer /= len(timers)
  print "here: ", mean_timer

  ## SYNC_PULL and SYNC_PUSH total average over runs.
  for i in range(0, int(numRuns)):
    # find sync_pull
    sync_pull_regex = re.compile(r'\[' + re.escape(forHost) + r'\]STAT,\(NULL\),SYNC_PULL_(?i)' + re.escape(benchmark) + r'\w*_' + re.escape(str(i)) + r'_(\d*),\d*,(\d*),(\d*).*')
    sync_pull_lines = re.findall(sync_pull_regex, log_data)
    for j in range (0, len(sync_pull_lines)):
      sync_pull_avg_time_total += float(sync_pull_lines[j][2])

    # find sync_push
    sync_push_regex = re.compile(r'\[' + re.escape(forHost) + r'\]STAT,\(NULL\),SYNC_PUSH_(?i)' + re.escape(benchmark) + r'\w*_'+ re.escape(str(i)) + r'_(\d*),\d*,(\d*),(\d*).*')
    sync_push_lines = re.findall(sync_push_regex, log_data)
    print benchmark
    print sync_push_lines
    for j in range (0, len(sync_push_lines)):
      sync_push_avg_time_total += float(sync_push_lines[j][2])

  sync_pull_avg_time_total /= int(numRuns)
  sync_push_avg_time_total /= int(numRuns)

  ## sendBytes and recvBytes.
  recvBytes_regex = re.compile(r'\[' + re.escape(forHost) + r'\]STAT,\(NULL\),RecvBytes,\d*,(\d*),(\d*),.*')
  recvBytes_search = recvBytes_regex.search(log_data)
  if recvBytes_search is not None:
     recvBytes_total = float(recvBytes_search.group(1))/int(numRuns)

  sendBytes_regex = re.compile(r'\[' + re.escape(forHost) + r'\]STAT,\(NULL\),SendBytes,\d*,(\d*),(\d*),.*')
  sendBytes_search = sendBytes_regex.search(log_data)
  if sendBytes_search is not None:
    sendBytes_total = float(sendBytes_search.group(1))/int(numRuns)

  ## sendBytes and recvBytes.
  recvNum_regex = re.compile(r'\[' + re.escape(forHost) + r'\]STAT,\(NULL\),RecvNum,\d*,(\d*),(\d*),.*')
  recvNum_search = recvNum_regex.search(log_data)
  if recvNum_search is not None:
    recvNum_total = float(recvNum_search.group(1))/int(numRuns)

  sendNum_regex = re.compile(r'\[' + re.escape(forHost) + r'\]STAT,\(NULL\),SendNum,\d*,(\d*),(\d*),.*')
  sendNum_search = sendNum_regex.search(log_data)
  if sendNum_search is not None:
    sendNum_total = float(sendNum_search.group(1))/int(numRuns)

  ## Get Graph_init, HG_init, total
  timer_graph_init_regex = re.compile(r'\[' + re.escape(forHost) + r'\]STAT,\(NULL\),TIMER_GRAPH_INIT,' + re.escape(numThreads) + r',(\d*),(\d*).*')
  timer_hg_init_regex = re.compile(r'\[' + re.escape(forHost) + r'\]STAT,\(NULL\),TIMER_HG_INIT,' + re.escape(numThreads) + r',(\d*),(\d*).*')
  timer_total_regex = re.compile(r'\[' + re.escape(forHost) + r'\]STAT,\(NULL\),TIMER_TOTAL,' + re.escape(numThreads) + r',(\d*),(\d*).*')


  timer_graph_init = timer_graph_init_regex.search(log_data)
  timer_hg_init = timer_hg_init_regex.search(log_data)
  timer_total = timer_total_regex.search(log_data)

  if timer_graph_init is not None:
    graph_init_time = timer_graph_init.group(1)

  if timer_hg_init is not None:
    hg_init_time = timer_hg_init.group(1)

  if timer_total is not None:
    total_time = timer_total.group(1)

#[13]STAT,PageRank,Commits,15,6377945,277895,324235,482281,296898,572496,295661,311751,434026,421630,445072,711824,444553,408666,535821,415136
#[13]STAT,PageRank,Conflicts,15,3167,196,281,296,210,438,288,203,304,135,128,213,111,106,152,106
#[13]STAT,PageRank,Iterations,15,6381112,278091,324516,482577,297108,572934,295949,311954,434330,421765,445200,712037,444664,408772,535973,415242
#[13]STAT,PageRank,Pushes,15,26999,3263,1940,2700,3747,2227,1977,2536,2264,694,895,720,1220,864,1006,946
  ## Get Commits, Conflicts, Iterations, Pushes for worklist versions:
  commits_search = re.compile(r'\[' + re.escape(forHost) + r'\]STAT,(\d*),Commits,' + re.escape(numThreads) + r',(\d*),(\d*).*').search(log_data)
  conflicts_search = re.compile(r'\[' + re.escape(forHost) + r'\]STAT,(\d*),Conflicts,' + re.escape(numThreads) + r',(\d*),(\d*).*').search(log_data)
  iterations_search = re.compile(r'\[' + re.escape(forHost) + r'\]STAT,(\d*),Iterations,' + re.escape(numThreads) + r',(\d*),(\d*).*').search(log_data)
  pushes_search = re.compile(r'\[' + re.escape(forHost) + r'\]STAT,(\d*),Pushes,' + re.escape(numThreads) + r',(\d*),(\d*).*').search(log_data)

  commits    = 0
  conflicts  = 0
  iterations = 0
  pushes     = 0
  if commits_search is not None:
    commits = commits_search.group(2)
  if conflicts_search is not None:
    conflicts = conflicts_search.group(2)
  if iterations_search is not None:
    iterations = iterations_search.group(2)
  if pushes_search is not None:
    pushes = pushes_search.group(2)


  return mean_timer,graph_init_time,hg_init_time,total_time,sync_pull_avg_time_total,sync_push_avg_time_total,recvNum_total,recvBytes_total,sendNum_total,sendBytes_total#,commits,conflicts,iterations, pushes

def get_basicInfo(fileName):

  hostNum_regex = re.compile(r'Hosts\s:\s(\d*)')
  cmdLine_regex = re.compile(r'CommandLine\s:\s(.*)')
  threads_regex = re.compile(r'Threads\s:\s(\d*)')
  runs_regex = re.compile(r'Runs\s:\s(\d*)')

  log_data = open(fileName).read()

  hostNum    = ''
  cmdLine    = ''
  threads    = ''
  runs       = ''
  benchmark  = ''
  algo_type  = ''
  cut_type   = ''
  input_type = ''



  hostNum_search = hostNum_regex.search(log_data)
  if hostNum_search is not None:
    hostNum = hostNum_search.group(1)

  cmdLine_search = cmdLine_regex.search(log_data)
  if cmdLine_search is not None:
    cmdLine = cmdLine_search.group(1)

  threads_search = threads_regex.search(log_data)
  if threads_search is not None:
    threads = threads_search.group(1)

  runs_search    = runs_regex.search(log_data)
  if runs_search is not None:
    runs = runs_search.group(1)

  split_cmdLine_algo = cmdLine.split()[0].split("/")[-1].split("_")
  benchmark, algo_type, cut_type =  split_cmdLine_algo

  split_cmdLine_input = cmdLine.split()[1].split("/")
  input_type = split_cmdLine_input[-1]

  return hostNum, cmdLine, threads, runs, benchmark, algo_type, cut_type, input_type

def main(argv):
  inputFile = ''
  forHost = '0'
  try:
    opts, args = getopt.getopt(argv,"hi:n:",["ifile=","node="])
  except getopt.GetoptError:
    print 'abelian_log_parser.py -i <inputFile> -n <hostNumber 0 to hosts - 1 >'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'abelian_log_parser.py -i <inputFile>'
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputFile = arg
    elif opt in ("-n", "--node"):
      forHost = arg

  print 'Input file is : ', inputFile
  print 'Data for host : ', forHost

  hostNum, cmdLine, threads, runs, benchmark, algo_type, cut_type, input_type = get_basicInfo(inputFile)
  print 'Hosts : ', hostNum , ' CmdLine : ', cmdLine, ' Threads : ', threads , ' Runs : ', runs, ' benchmark :' , benchmark , ' algo_type :', algo_type, ' cut_type : ', cut_type, ' input_type : ', input_type

  #mean_timer,recvNum_total,recvBytes_total,sendNum_total,sendBytes_total,sync_pull_avg_time_total,sync_push_avg_time_total,graph_init_time,hg_init_time,total_time = match_timers(inputFile, forHost, runs, threads)
  data = match_timers(inputFile, benchmark, forHost, runs, threads)

  print data

  output_str = benchmark + ',' + 'abelian'  + ',' + hostNum  + ',' + threads  + ',' + input_type  + ',' + algo_type  + ',' + cut_type

  for d in data:
    output_str += ','
    output_str += str(d)
  print output_str

  new_data = output_str.split(",") + list(data)
  myfile = open("myfile_output.csv", 'a')
  wr = csv.writer(myfile, quoting=csv.QUOTE_NONE, lineterminator='\n')
  wr.writerow(new_data)
  myfile.close()


if __name__ == "__main__":
  main(sys.argv[1:])

