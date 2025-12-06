WIDTH, HEIGHT = 800, 600
BAR_WIDTH = 40
BAR_GAP = 5
UI_HEIGHT = 80 + 1
BG_COLOR = (30, 30, 30)

data = [1, 2, 3, 4, 5, 6, 7, 8]

COLORS = {
    "default": (100, 200, 255),
    "insert": (255, 200, 0),
    "rotate": (255, 120, 120)
}

def graph_setup(screen, font_m, font_s, alg):
    # ------ Algorithm Title ------
    surf = font_m.render(alg.capitalize() + "Tree", True, (255, 255, 255))
    rect = surf.get_rect(center=(WIDTH // 2, 120 ))
    screen.blit(surf, rect)

def solve(s, t):
    flag = 1
    for ch in s:
        if ch in t:
            t.remove(ch)
        else:
            print("Impossible")
            flag = 0
            break
    
    if flag:
        n = len(s)
        i = 0
        pairs = []
        while i < len(s):
            l = r = i
            while r < n - 1 and s[r+1] < s[l]:
                r += 1
            pairs.append((l, r))
            i = r + 1
    
        t.sort()

        m = len(t)
        i = j = 0
        chars = []
        while i < m and j < len(pairs):
            if t[i] < s[pairs[j][0]]:
                chars.append(t[i])
                i += 1
            else:
                l, r = pairs[j]
                for k in range(l, r+1):
                    chars.append(s[k])
                j += 1
        
        while i < m:
            chars.append(t[i])
            i += 1
        
        while j < len(pairs):
            l, r = pairs[j]
            for k in range(l, r+1):
                chars.append(s[k])
            j += 1
        
        print("".join(chars))

solve("babadab", list("abacabadabacaba"))