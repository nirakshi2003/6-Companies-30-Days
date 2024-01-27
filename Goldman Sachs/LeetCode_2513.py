class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        """
        :type divisor1: int
        :type divisor2: int
        :type uniqueCnt1: int
        :type uniqueCnt2: int
        :rtype: int
        """
        l = 1
        r = 10 ** 15
        ans = r
        d1 = divisor1
        d2 = divisor2
        cnt1 = uniqueCnt1
        cnt2 = uniqueCnt2

        g = self.gcd(d1, d2)
        lcm = (d1 * d2) // g

        while l <= r:
            mid = (l + r) // 2

            if d1 == d2:
                cnt = mid - (mid // d1)
                if cnt >= cnt1 + cnt2:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                common = mid // lcm
                c1 = (mid // d1) - common
                c2 = (mid // d2) - common

                z1 = cnt1
                z2 = cnt2
                avail = mid - (c1 + c2 + common)

                z1 -= min(z1, c2)
                z1 -= min(z2, c1)

                if z1 + z2 <= avail:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1

        return ans
