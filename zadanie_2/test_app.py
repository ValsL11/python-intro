import unittest
import math
import coverage
from parameterized import parameterized
from app import isEmailCorrect, isPalindrome, calcCircleArea, sortArr, convertDateFormat

# Testy dla funkcji sprawdzającej poprawność adresu email
class TestIsEmailCorrect(unittest.TestCase):
  @parameterized.expand([
    # Poprawne adresy email
    ("validEmail", "test@example.com", True),  # Prosty poprawny adres email
    ("validEmailWithNumbers", "user123@domain123.com", True),  # Poprawny adres email z liczbami w nazwie użytkownika i domenie
    ("validEmailWithSubdomain", "user@sub.domain.com", True),  # Email z subdomeną
    ("validEmailWithHyphen", "user-name@domain.com", True),  # Email z myślnikiem w nazwie użytkownika
    ("validEmailWithDotBeforeDomain", "user.name@domain.com", True),  # Email z kropką przed domeną
    ("validEmailWithDotInDomain", "user@domain.co.uk", True),  # Email z domeną składającą się z kilku poziomów

    # Niepoprawne adresy email
    ("invalidEmailNoAtSymbol", "testexample.com", False),  # Brak symbolu @
    ("invalidEmailNoDomain", "test@.com", False),  # Brak części domenowej po @
    ("invalidEmailNoTld", "test@domain", False),  # Brak TLD (np. .com, .org)
    ("invalidEmailNoUsername", "@domain.com", False),  # Brak nazwy użytkownika
    ("invalidEmailMultipleAt", "test@@example.com", False),  # Podwójny symbol @
    ("invalidEmailSpaceInDomain", "test@exa mple.com", False),  # Spacja w domenie
    ("invalidEmailWithSpecialChars", "user#domain@domain.com", False),  # Niepoprawny znak specjalny w nazwie użytkownika
    ("emptyEmail", "", False),  # Pusty ciąg znaków to niepoprawny email
    ("emailWithMultipleSubdomains", "user@sub.sub.domain.com", True),  # Poprawny email z wieloma subdomenami
    ("emailWithNumbersInDomain", "user@domain123.com", True),  # Poprawny email z liczbami w domenie
    ("emailWithSpecialCharsInDomain", "user@doma!n.com", False),  # Niepoprawny email z nieprawidłowym znakiem w domenie
  ])
  def testIsEmailCorrect(self, name, email, expectedResult):
    # Sprawdzamy, czy wynik działania funkcji isEmailCorrect odpowiada oczekiwanemu wyniku
    self.assertEqual(isEmailCorrect(email), expectedResult)

# Testy dla funkcji sprawdzającej, czy tekst jest palindromem
class TestIsPalindrome(unittest.TestCase):
  @parameterized.expand([
    # Poprawne palindromy
    ("validPalindrome", "Kajak", True),  # Palindrom - duże litery
    ("invalidPalindrome", "Ala ma kota", False),  # Niepalindrom - z przerwami i literami w innych miejscach
    ("validPalindromeWithSpaces", "A to kanapa pana Kota", True),  # Palindrom - z przestrzeniami
    ("palindromeWithPunctuation", "Eva, can I see bees in a cave?", True),  # Palindrom - z interpunkcją
    ("emptyString", "", True),  # Pusty ciąg znaków to palindrom
    ("singleCharacter", "a", True),  # Pojedynczy znak to palindrom
    ("validPalindromeMixedCase", "MadAm", True),  # Palindrom z mieszanymi literami
    ("validPalindromeSpecialChars", "A man, a plan, a canal, Panama!", True),  # Palindrom z znakami specjalnymi
  ])
  def testPalindrome(self, name, text, expectedResult):
    # Sprawdzamy, czy funkcja isPalindrome zwróciła oczekiwany wynik
    self.assertEqual(isPalindrome(text), expectedResult)

# Testy dla funkcji obliczającej pole koła
class TestCalcCircleArea(unittest.TestCase):
  def setUp(self):
    # Ustawiamy dane testowe: promienie o różnych wartościach
    self.radiusZero = 0
    self.radiusOne = 1
    self.radiusFloat = 3.7
    self.radiusLarge = 1000
    self.negativeRadius = -5
    self.extremelyLargeRadius = 1e6  # Bardzo duży promień
    self.smallRadius = 1e-6  # Bardzo mały promień

  def testAreaOne(self):
    # Testujemy, czy pole dla promienia 1 jest równe π
    self.assertAlmostEqual(calcCircleArea(self.radiusOne), math.pi)

  def testAreaFloat(self):
    # Testujemy, czy pole dla promienia zmiennoprzecinkowego jest obliczane poprawnie
    self.assertAlmostEqual(calcCircleArea(self.radiusFloat), math.pi * self.radiusFloat ** 2)

  def testAreaLarge(self):
    # Testujemy, czy pole dla bardzo dużego promienia jest obliczane poprawnie
    self.assertAlmostEqual(calcCircleArea(self.radiusLarge), math.pi * self.radiusLarge ** 2)

  def testExtremelyLargeRadius(self):
    # Testujemy, czy pole dla ekstremalnie dużego promienia jest obliczane poprawnie
    self.assertAlmostEqual(calcCircleArea(self.extremelyLargeRadius), math.pi * self.extremelyLargeRadius ** 2)

  def testSmallRadius(self):
    # Testujemy, czy pole dla ekstremalnie małego promienia jest obliczane poprawnie
    self.assertAlmostEqual(calcCircleArea(self.smallRadius), math.pi * self.smallRadius ** 2)
  
  def testNegativeOrZeroRadius(self):
    # Testujemy, czy dla promieni 0 i ujemnych pojawi się wyjątek
    with self.assertRaises(ValueError):
        calcCircleArea(self.radiusZero)
    with self.assertRaises(ValueError):
        calcCircleArea(self.negativeRadius)

# Testy dla funkcji sortującej tablicę
class TestSortArr(unittest.TestCase):
  def setUp(self):
    # Ustawiamy dane testowe: różne przypadki tablic
    self.sortedList = [1, 2, 3, 4, 5]
    self.unsortedList = [5, 3, 1, 4, 2]
    self.listWithDuplicates = [4, 2, 4, 3, 1]
    self.negativeNumbers = [-2, -5, -1, -3]
    self.emptyList = []
    self.largeArray = list(range(1000, 0, -1))  # Duża tablica w odwrotnej kolejności

  def testSortedList(self):
    # Testujemy, czy posortowana lista jest prawidłowa
    self.assertEqual(sortArr(self.sortedList), sorted(self.sortedList))

  def testUnsortedList(self):
    # Testujemy, czy nieposortowana lista zostanie posortowana poprawnie
    self.assertEqual(sortArr(self.unsortedList), sorted(self.unsortedList))

  def testListWithDuplicates(self):
    # Testujemy, czy lista z duplikatami zostanie prawidłowo posortowana
    self.assertEqual(sortArr(self.listWithDuplicates), sorted(self.listWithDuplicates))

  def testNegativeNumbers(self):
    # Testujemy, czy lista z liczbami ujemnymi zostanie prawidłowo posortowana
    self.assertEqual(sortArr(self.negativeNumbers), sorted(self.negativeNumbers))

  def testEmptyList(self):
    # Testujemy, czy pusta lista zostanie poprawnie obsłużona
    self.assertEqual(sortArr(self.emptyList), [])
  
  def testLargeArray(self):
    # Testujemy, czy bardzo duża lista zostanie poprawnie posortowana
    self.assertEqual(sortArr(self.largeArray), sorted(self.largeArray))

# Testy dla funkcji konwertującej format daty
class TestConvertDateFormat(unittest.TestCase):
  @parameterized.expand([
      ("test_case_1", "2025-03-29", "%Y-%m-%d", "%d/%m/%Y", "29/03/2025"),  # Standardowy przypadek
      ("test_case_2", "2021-07-15", "%Y-%m-%d", "%d/%m/%Y", "15/07/2021"),  # Standardowy przypadek
      ("test_case_3", "1999-12-31", "%Y-%m-%d", "%d/%m/%Y", "31/12/1999"),  # Standardowy przypadek
  ])
  def testConvertDateFormatStandard(self, name, dateStr, inputFormat, outputFormat, expectedResult):
      # Testujemy konwersję daty w formacie standardowym
      self.assertEqual(convertDateFormat(dateStr, inputFormat, outputFormat), expectedResult)

  @parameterized.expand([
      ("test_case_4", "29.03.2025", "%d.%m.%Y", "%Y/%m/%d", "2025/03/29"),  # Data z kropkami
      ("test_case_5", "15.07.2021", "%d.%m.%Y", "%Y/%m/%d", "2021/07/15"),  # Data z kropkami
      ("test_case_6", "31.12.1999", "%d.%m.%Y", "%Y/%m/%d", "1999/12/31"),  # Data z kropkami
  ])
  def testConvertDateFormatWithDots(self, name, dateStr, inputFormat, outputFormat, expectedResult):
      # Testujemy konwersję daty w formacie z kropkami
      self.assertEqual(convertDateFormat(dateStr, inputFormat, outputFormat), expectedResult)

if __name__ == '__main__':
    cov = coverage.Coverage()
    cov.start()

    try:
        unittest.main()
    except:  
        pass

    cov.stop()
    cov.save()

    # Raport z pokrycia kodu
    print(cov.report())