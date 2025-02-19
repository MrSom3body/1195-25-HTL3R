__author__ = "Karun Sandhu"

from collections import Counter
from .caesar import Caesar


class Kasiski:
    def __init__(self, crypttext: str = "") -> None:
        self.c: Caesar = Caesar()
        self.crypttext: str = self.c.to_lowercase_letter_only(crypttext)

    def allpos(self, text: str, substring: str) -> list[int]:
        """
        Calculates the positions of the substring in text.
        :param text: the text to look in
        :param substring: the substring to look for
        :return: a list with the indicies

        >>> k = Kasiski()
        >>> k.allpos("heissajuchei, ein ei", "ei")
        [1, 10, 14, 18]
        >>> k.allpos("heissajuchei, ein ei", "hai")
        []
        """
        return [
            i
            for i in range(len(text) - len(substring) + 1)
            if text[i : i + len(substring)] == substring
        ]

    def alldist(self, text: str, substring: str) -> set[int]:
        """
        Calculate all distances between all occurences of substring in text.
        :param text: the text to look in
        :param substring: the substring to look for
        :return: a list with the distances

        >>> k = Kasiski()
        >>> k.alldist("heissajuchei, ein ei", "ei")
        {4, 8, 9, 13, 17}
        >>> k.alldist("heissajuchei, ein ei", "hai")
        set()
        """
        dist: set[int] = set()
        pos = self.allpos(text, substring)
        for i in range(len(pos)):
            for j in range(i + 1, len(pos)):
                dist.add(pos[j] - pos[i])
        return dist

    def dist_n_tuple(self, text: str, length: int) -> set[tuple[str, int]]:
        """
        Checks all substrings of the text with the provided length and returns
        a set with all distances of all repetitions of the substring.
        :param text: the text to look in
        :param length: the lenght of the substrings to look for
        :return: a set containig tuples containing the substring and the distances
        
        >>> k = Kasiski()
        >>> k.dist_n_tuple("heissajuchei", 2) == {('ei', 9), ('he', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 3) == {('hei', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 4) == set()
        True
        >>> k.dist_n_tuple("heissajucheieinei", 2) == \
        {('ei', 5), ('ei', 14), ('ei', 3), ('ei', 9), ('ei', 11), ('he', 9), ('ei', 2)}
        True
        """
        dist_n: set[tuple[str, int]] = set()
        for i in range(len(text) - length + 1):
            substring = text[i : i + length]
            pos = self.allpos(text, substring)
            if len(pos) > 1:
                for dist in self.alldist(text, substring):
                    dist_n.add((substring, dist))
        return dist_n

    def dist_n_list(self, text: str, length: int) -> list[int]:
        """
        Checks all substrings of the text with the provided length and returns
        a list with all distances of all repetitions of the substring without
        the substring. It also removes duplicate distances and sorts the list
        ascending.
        :param text: the text to look in
        :param length: the lenght of the substrings to look for
        :return: a list containing the distances

        >>> k = Kasiski()
        >>> k.dist_n_list("heissajucheieinei", 2)
        [2, 3, 5, 9, 11, 14]
        >>> k.dist_n_list("heissajucheieinei", 3)
        [9]
        >>> k.dist_n_list("heissajucheieinei", 4)
        []
        """
        return [*set([elem[1] for elem in self.dist_n_tuple(text, length)])]

    def gcd(self, x: int, y: int) -> int:
        """
        Calculates the greatest common divisor of two integers.
        :param x: first integer
        :param y: second integer
        :return: greatest common divisor

        >>> k = Kasiski()
        >>> k.gcd(10, 25)
        5
        >>> k.gcd(48, 18)
        6
        """
        if min(x, y) == 0:
            return max(x, y)
        else:
            return self.gcd(min(x, y), max(x, y) % min(x, y))

    def gcd_count(self, numbers: list[int]) -> Counter[int]:
        """
        Gets the greatest common divisor of all the combinations in numbers.
        :param numbers: the list with the numbers
        :return: the counter with all the gcd's

        >>> k = Kasiski()
        >>> k.gcd_count([12, 14, 16])
        Counter({2: 2, 12: 1, 4: 1, 14: 1, 16: 1})
        >>> k.gcd_count([10, 25, 50, 100])
        Counter({10: 3, 25: 3, 50: 2, 5: 1, 100: 1})
        """
        gcds: list[int] = []
        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                gcds.append(self.gcd(numbers[i], numbers[j]))
        return Counter(gcds)

    def get_nth_letter(self, s: str, start: int, n: int) -> str:
        """
        Extracts every n-th letter after start.
        :param s: the string to pick the letters out of
        :param start: the index to start after
        :param n: interval to select the letter

        >>> k = Kasiski()
        >>> k.get_nth_letter("Das ist kein kreativer Text.", 1, 4)
        'asektrx'
        """
        return "".join([ch for ch in s[start::n]])

    def crack_key(self, length: int) -> str:
        """
        Gets the most likely key for the encrypted text by looking for repeating
        patterns with the provided length.
        :param length: the lentgh of the repeating patterns to look for
        :return: the most probable key

        >>> ciphertext = "LMTFMAOSMMMTPRTPABFEUIZQTEFECRCIGHMARAKXMAOEKDIHMEKMVHYDASTGPSXMVRCFKECRTNXLIAOVHPTELPNRHRWNLMMZLCAXMFTCAWWTWEBGPFLLTXLNCANWCAOALWQUYVHPTRCBXKQRCDXECSDIXLIGEEGMPELBXVABRUMKMFNHFIKXEDTWAFTEWIVNYDXVVGLGGSKUORXMUNWSHZQRWLNWBQLRTYNOPKTQIYDOZMVTOEKQIAYAFEJRYDPMMQPRAMVNMAEWMELBXVLVPMTYMESEKEJTPKEIBGPRMAIEPRLGPELKXVORHAEXQTOEGRMEDAAHQRKANFMETNOSZFTCAWBRSEGAQRVAGRAGOUXWENREGWXELCAWQRXIMDWEYIZIUOWIVOQAXEBRMARAKXMAKULXMVREGYVQHIXIQAOIXFUVCMXMVRCAIYVMPLGDCFEEAPMAOALWWYWDBVAPSLXGPGMEDSUZPNTGPNYTPSZGPTXHMEXAGRDRCZXMPGXIKFQGEEBGPULBXQQPSNNVIHDNHXLNKUXRBFNHESAFPNFIQAPFKECULTXYZRCAIYVMPLGECFOEFJMADTXVMEMLBGSGFNWIUCQAGHMVYSHKZBDSXWDRCLTRORYDTWAFTELXMEMEGACRCDXAMAYSBIVVNHMHIIZNSYMFDEGFMXZMFXABRLXMKUQIXPMAOIXLINCEAIZNMUGHMEDTBIOUTNTYNNYFTROFPRLGPELKKEXHYZXPORHAEXQTLLLIQAXAGRHHTHKLMEPIGOIZHIXMPEPANKMAYOVLVVPEBRMAPRUPQPVTAEBGPNWSKUOEKOWRYIZWABSNYMVTLNZEVMQRXYVQWIVLUVEIAVHHCEWIVHYDXVHNPHEXMVSRWEAFGOGMPEPMZIANYGLIQASEKDABDEAVJRHEZXEBCDXRARTDTWARDIAQSRTNXVCUPGXPIFDEGLIGFNWIZFTELITODTAEJRDEAIVZFELWMAOAOIZYZRKEXHYZXPQUCETROFEUGHIYDEKWQRQRTKBRZBLMMVSNSYUZLNGRMUXEGAWYWTXYVQDIXWIUOALWMEUUGKCAOSVLWRYWTVABOAVLBRDIXHMEHIKHUVNHEMMOPRAEJRYAEWLVPAEXMSCANKWGPLNRLFLGMIRNFNWPMTEEBLZRSAGHQADEBRMULNWWQRDPKEKUTCAAQYWGXVVRXIMHQEREAIVJPNGHCXZMFWBFZBKMVTUEWIAZLLXMVRYSMVIARSXMLRXIMHIELULAQYWIVLMVYEEIQGPRYPMPSTXRCAOWXRVQTEYIZGTGBWBFZSMIQTPIVLPRCUGXMEFNWHCATMFWBZTCAECSOEBRXSPRWWQRGEKEJEPDXXMAOALWMEMILHIUTNCILRYAUIVQKUBLZXZMFIVFZLEXMQPNGFMVEAZOIZOIXETGPAFEJRYDLXQRREKETFZUXFMEOIXQIHPRBRLRYGTVBRYDXVHNFBXVQAFNWLWYEELIQAPRYVIHPIGIPNYDOSTYCAIYVMPLGWQRXAVLBRDIVLABRLXMKUDAEEBQLRTYAHYDTWAVSNOSTYPRUIOVPRWIIHQSBIPNETXRQUCAUIZFZGNXORDCAQMPVTWEAFDIXHMALNWIZAEAZRWPSDKIQZLLLSDVPLEYAGOAKECSMEDEUNWSHKQARDXVUNYNTQIOPNWAQROEKLQALBTPARCAUIZQTEFECRCHXVIOREDPMGEEKXENCEKWKUCADIZTPWTPBVRDXRVRCSTLLVPZTYJRCIGZWEDIVLAGPHXREVPKTRVFEDNIAJLGXRACCAVLAVPMBXHBCNBKMZMLBGSVYMXMVRYGTVBRYZNWBRTGXRCAOWBIMVYDBIJZTRFIQAPRTTCAKEERHHDTXLTRYDTWABWLWMZFNHEIKUEBXOWZXEGEKULNMAWEEEMILRCMTRVIPRSIQUEMBVJVETXMKUSAUIUVNHGYZNFSGSBQLZNIVGDCAPWFDEGQMVYEYVIHSAMICEPRTTCAKEERIHDDXQNRYSMIZRCBEMKXEUGHMZAFTRLRTNLSOEZSLIAIPREEVTPNWEAFDIXWBRCBXREHPRWIERYNLMMATCAXLNGOGDCRDSXRJRVOFQBFZGEIQPSFBITRYDBIPNLRXLMELBNRLRCSMMMTSIGECSLNYEVTDEKWKUCADVICFNSITTPWTPBVRAEWMVYMTRVMFIAVPRCEBRSNXWBIQUCETYORYNHGPATEXMVRYEKFTVNKMLIGEEGHWPSDXVSBPNBKAFZHGJQARAGKIAKFKICAOLBGPZTTBLZMFRXHMAFNWIZMLEAPBRTHKHIFDVHRQUCEFKMFLNZWMVYHXVHFZSXLZOPWXKBJZRWIVFPIWEAFPSBLUXPIGIZHSEZITNDSXRPNEUGHMEDIXWMYMSMLIOPSXLMAXUXWARYDTZMEWOKVICFNSITVSRXEVTDTNRLNWSXVAVPFKEOGPOUWQRTHGDCZXAGRVRSMXREBWLMICAOSBIANSDTWARCJNROHYDLGPBPNPEZFZDTGPGPSBILRCWBVLZTCAPQRMEKLIOPNTPAQTETPBRQRTYOBEEEYVQDAZXMWLUGHTRRTXMPEPHTRLVYSXMVRSAGHAVPSIVIPSIVLEVWLZIZAPMBXLVCGXLMAHEGRLHVOFQAGDOUVQARJXHMFXAEIQAPNLXZNYGLIQQPMBXLNCANWEVWLBGPRTNXPMVEEKJTRNHMIVHYDPIVAOIXJMEEIZMAGDOLXMVREBGPUPRNRBRCUGHLHYIFQAGXIVLIHQDXMVCQEKHAVPVXVIOCEWIBRYDTWARCBBWLNSIGNMQPNTFMAOZNMPEVOFQMADOEPBROEGRJRTTTKSNXDBIIYEE"
        >>> k = Kasiski(ciphertext)
        >>> k.crack_key(3)
        'latein'
        >>> k.crack_key(7)
        'latein'
        >>> k.crack_key(11)
        Traceback (most recent call last):
        ...
        ValueError: Text is too short or the key length is too long.
        """
        key = ""
        distances = self.dist_n_list(self.crypttext, length)
        if len(distances) < 2:
            raise ValueError("Text is too short or the key length is too long.")
        gcds = self.gcd_count(distances).most_common()
        key_length = gcds[0][0] if gcds[0][0] != 1 else gcds[1][0]
        for i in range(key_length):
            key += self.c.crack(
                self.get_nth_letter(self.crypttext, i, key_length)
            )[0]
        return key


if __name__ == "__main__":
    import doctest

    _ = doctest.testmod()
