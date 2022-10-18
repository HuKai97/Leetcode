# https://www.bilibili.com/video/BV1nK4y147ZF?spm_id_from=333.337.search-card.all.click&vd_source=5f6bbc1038b075757cb446f800f3cd56
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def checkIPv4(ip):
            for s in ip:
                # check length
                if len(s) < 1 or len(s) > 3: return 'Neither'
                # check digit
                for i in range(len(s)):
                    if s[i] < '0' or s[i] > '9': return 'Neither'
                # check leading zero
                if len(s) > 1 and s[0] == '0': return 'Neither'
                # check range
                if len(s) == 3:
                    cur_sum = 0
                    for i in range(len(s)):
                        cur_sum = cur_sum * 10 + int(s[i])
                    if cur_sum > 255: return 'Neither'
            return 'IPv4'

        def checkIPv6(ip):
            for s in ip:
                # check lenght
                if len(s) < 1 or len(s) > 4: return 'Neither'
                # check digit
                for i in range(len(s)):
                    if '0'<=s[i]<='9' or 'a'<=s[i]<='f': continue
                    return 'Neither'
            return 'IPv6'

        ip = queryIP.lower()
        ipv4 = ip.split('.')
        if len(ipv4) == 4:
            return checkIPv4(ipv4)
        ipv6 = ip.split(':')
        if len(ipv6) == 8:
            return checkIPv6(ipv6)
        return 'Neither'
