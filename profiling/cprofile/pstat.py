import pstats
p = pstats.Stats('output.prof')
p.sort_stats('cumtime')
p.print_stats()