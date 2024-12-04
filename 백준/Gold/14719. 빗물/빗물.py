def solution():
    H,W = map(int,input().split())
    blocks = list(map(int,input().split()))
    
    max_hts=max(blocks)
    max_hts_idx = blocks.index(max_hts)
    
    total_area = 0
    current_hts=blocks[0]
    
    for i in range(max_hts_idx):
        current_hts = max(current_hts,blocks[i])
        total_area+=current_hts
        
    current_hts = blocks[-1]
    for i in range(W-1,max_hts_idx,-1):
        current_hts= max(current_hts,blocks[i])
        total_area+=current_hts
    
    total_area+=max_hts
    
    ans = total_area - sum(blocks)
    print(ans)
solution()
        