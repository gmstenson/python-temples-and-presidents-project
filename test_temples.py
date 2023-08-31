from temples import read_dict, days_between
import pytest
from datetime import datetime
from os import path

PRESIDENT_INDEX = 0
BIRTHDATE_INDEX = 1
ORDINATION_INDEX = 2
DEATH_INDEX = 3
PRESIDENT_TEMPLE_ANNOUNCEMENTS_INDEX = 4
PRESIDENT_TEMPLE_GROUNDBREAKINGS_INDEX = 5
PRESIDENT_TEMPLE_DEDICATIONS_INDEX = 6
TEMPLE_NAME_INDEX = 0
TEMPLE_ANNOUNCED_INDEX = 1
TEMPLE_GROUNDBREAKING_INDEX = 2
TEMPLE_DEDICATION_INDEX = 3
TEMPLE_NUMBER_SEALING_ROOMS_INDEX = 4
TEMPLE_SQFT_INDEX = 5

def test_read_dict():
    """Verify that the read_dict function works correctly.
    Parameters: none
    Return: nothing
    """

    # Call the read_dict function and store the returned
    # dictionary in a variable named presidents_dict.
    filename = path.join(path.dirname(__file__), "presidents.csv")
    presidents_dict = read_dict(filename, PRESIDENT_INDEX)

    # Verify that the read_dict function returns a dictionary.
    assert isinstance(presidents_dict, dict), \
        "read_dict function must return a dictionary:" \
        f" expected a dictionary but found a {type(presidents_dict)}"

    # Verify that the presidents dictionary contains exactly 17 items.
    length = len(presidents_dict)
    exp_len = 17
    assert length == exp_len, \
        "presidents dictionary has too" \
        f" {'few' if length < exp_len else 'many'} items:" \
        f" expected {exp_len} but found {length}"

    # Check each item in the presidents dictionary.
    check_president(presidents_dict, "Joseph Smith", ["Joseph Smith", "23-Dec-1805", "6-Apr-1830", "27-Jun-1844", 5, 3, 1])
    check_president(presidents_dict, "Brigham Young", ["Brigham Young", "1-Jun-1801", "27-Dec-1847", "29-Aug-1877", 4, 4, 2])
    check_president(presidents_dict, "John Taylor", ["John Taylor", "1-Nov-1808", "10-Oct-1880", "25-Jul-1887", 0, 0, 1])
    check_president(presidents_dict, "Wilford Woodruff", ["Wilford Woodruff", "1-Mar-1807", "7-April-1889", "2-Sept-1898", 0, 0, 2])
    check_president(presidents_dict, "Lorenzo Snow", ["Lorenzo Snow", "3-Apr-1814", "13-Sept-1898", "10-Oct-1901", 0, 0, 0])
    check_president(presidents_dict, "Joseph F Smith", ["Joseph F Smith", "13-Nov-1838", "17-Oct-1901", "19-Nov-1918", 2, 2, 0])
    check_president(presidents_dict, "Heber J Grant", ["Heber J Grant", "22-Nov-1856", "23-Nov-1918", "14-May-1945", 3, 2, 3])
    check_president(presidents_dict, "George Albert Smith", ["George Albert Smith", "4-Apr-1870", "21-May-1945", "4-Apr-1951", 0, 0, 1])
    check_president(presidents_dict, "David O McKay", ["David O McKay", "8-Sep-1873", "9-Apr-1951", "18-Jan-1970", 7, 8, 5])
    check_president(presidents_dict, "Joseph Fielding Smith", ["Joseph Fielding Smith", "19-Jul-1876", "23-Jan-1970", "2-Jul-1972", 0, 0, 2])
    check_president(presidents_dict, "Harold B Lee", ["Harold B Lee", "28-Mar-1899", "7-Jul-1972", "26-Dec-1973", 0, 0, 0])
    check_president(presidents_dict, "Spencer W Kimball", ["Spencer W Kimball", "28-Mar-1895", "30-Dec-1973", "5-Nov-1985", 31, 25, 21])
    check_president(presidents_dict, "Ezra Taft Benson", ["Ezra Taft Benson", "4-Aug-1899", "10-Nov-1985", "30-May-1994", 9, 10, 9])
    check_president(presidents_dict, "Howard W Hunter", ["Howard W Hunter", "14-Nov-1907", "5-Jun-1994", "3-Mar-1995", 3, 1, 2])
    check_president(presidents_dict, "Gordon B Hinckley", ["Gordon B Hinckley", "23-Jun-1910", "12-Mar-1995", "27-Jan-2008", 79, 81, 77])
    check_president(presidents_dict, "Thomas S Monson", ["Thomas S Monson", "21-Aug-1927", "3-Feb-2008", "2-Jan-2018", 45, 37, 35])
    check_president(presidents_dict, "Russell M Nelson", ["Russell M Nelson", "9-Sep-1924", "14-Jan-2018", "N/A", 100, 54, 14])


    # Call the read_dict function and store the returned
    # dictionary in a variable named temples_dict.
    filename = path.join(path.dirname(__file__), "temples.csv")
    temples_dict = read_dict(filename, TEMPLE_NAME_INDEX)

    # Verify that the read_dict function returns a dictionary.
    assert isinstance(temples_dict, dict), \
        "read_dict function must return a dictionary:" \
        f" expected a dictionary but found a {type(temples_dict)}"

    # Verify that the temples dictionary contains exactly 175 items.
    length = len(temples_dict)
    exp_len = 175
    assert length == exp_len, \
        "temples dictionary has too" \
        f" {'few' if length < exp_len else 'many'} items:" \
        f" expected {exp_len} but found {length}"

    # Check each item in the temples dictionary.
    check_temple(temples_dict, "Aba Nigeria Temple", ["Aba Nigeria Temple", "2-Apr-2000", "23-Feb-2002", "7-Aug-2005", 2, 11500])
    check_temple(temples_dict, "Accra Ghana Temple", ["Accra Ghana Temple", "16-Feb-1998", "16-Nov-2001", "11-Jan-2004", 2, 17500])
    check_temple(temples_dict, "Adelaide Australia Temple", ["Adelaide Australia Temple", "17-Mar-1999", "29-May-1999", "15-Jun-2000", 2, 10700])
    check_temple(temples_dict, "Albuquerque New Mexico Temple", ["Albuquerque New Mexico Temple", "4-Apr-1997", "20-Jun-1998", "5-Mar-2000", 3, 34245])
    check_temple(temples_dict, "Anchorage Alaska Temple", ["Anchorage Alaska Temple", "4-Oct-1997", "17-Apr-1998", "9-Jan-1999", 1, 11937])
    check_temple(temples_dict, "Apia Samoa Temple", ["Apia Samoa Temple", "15-Oct-1977", "19-Feb-1981", "5-Aug-1983", 2, 18691])
    check_temple(temples_dict, "Arequipa Peru Temple", ["Arequipa Peru Temple", "6-Oct-2012", "4-Mar-2017", "15-Dec-2019", 2, 26969])
    check_temple(temples_dict, "Asuncion Paraguay Temple", ["Asuncion Paraguay Temple", "2-Apr-2000", "3-Feb-2001", "19-May-2002", 2, 11906])
    check_temple(temples_dict, "Atlanta Georgia Temple", ["Atlanta Georgia Temple", "2-Apr-1980", "7-Mar-1981", "1-Jun-1983", 4, 34500])
    check_temple(temples_dict, "Barranquilla Colombia Temple", ["Barranquilla Colombia Temple", "1-Oct-2011", "20-Feb-2016", "9-Dec-2018", 2, 24000])
    check_temple(temples_dict, "Baton Rouge Louisiana Temple", ["Baton Rouge Louisiana Temple", "14-Oct-1998", "8-May-1999", "16-Jul-2000", 2, 10890])
    check_temple(temples_dict, "Belem Brazil Temple", ["Belem Brazil Temple", "3-Apr-2016", "17-Aug-2019", "20-Nov-2022", 0, 0])
    check_temple(temples_dict, "Bern Switzerland Temple", ["Bern Switzerland Temple", "1-Jul-1952", "5-Aug-1953", "11-Sep-1955", 7, 35546])
    check_temple(temples_dict, "Billings Montana Temple", ["Billings Montana Temple", "30-Aug-1996", "30-Mar-1998", "20-Nov-1999", 3, 33800])
    check_temple(temples_dict, "Birmingham Alabama Temple", ["Birmingham Alabama Temple", "11-Sep-1998", "9-Oct-1999", "3-Sep-2000", 2, 10700])
    check_temple(temples_dict, "Bismarck North Dakota Temple", ["Bismarck North Dakota Temple", "29-Jul-1998", "17-Oct-1998", "19-Sep-1999", 2, 10700])
    check_temple(temples_dict, "Bogota Colombia Temple", ["Bogota Colombia Temple", "7-Apr-1984", "26-Jun-1993", "24-Apr-1999", 3, 53500])
    check_temple(temples_dict, "Boise Idaho Temple", ["Boise Idaho Temple", "31-Mar-1982", "18-Dec-1982", "25-May-1984", 4, 35868])
    check_temple(temples_dict, "Boston Massachusetts Temple", ["Boston Massachusetts Temple", "30-Sep-1995", "13-Jun-1997", "1-Oct-2000", 4, 69600])
    check_temple(temples_dict, "Bountiful Utah Temple", ["Bountiful Utah Temple", "2-Feb-1990", "2-May-1992", "8-Jan-1995", 8, 104000])
    check_temple(temples_dict, "Brigham City Utah Temple", ["Brigham City Utah Temple", "3-Oct-2009", "31-Jul-2010", "23-Sep-2012", 3, 36000])
    check_temple(temples_dict, "Brisbane Australia Temple", ["Brisbane Australia Temple", "20-Jul-1998", "26-May-2001", "15-Jun-2003", 2, 10700])
    check_temple(temples_dict, "Buenos Aires Argentina Temple", ["Buenos Aires Argentina Temple", "2-Apr-1980", "20-Apr-1983", "17-Jan-1986", 3, 30659])
    check_temple(temples_dict, "Calgary Alberta Temple", ["Calgary Alberta Temple", "4-Oct-2008", "15-May-2010", "28-Oct-2012", 3, 33000])
    check_temple(temples_dict, "Campinas Brazil Temple", ["Campinas Brazil Temple", "3-Apr-1997", "1-May-1998", "17-May-2002", 3, 48100])
    check_temple(temples_dict, "Caracas Venezuela Temple", ["Caracas Venezuela Temple", "30-Sep-1995", "10-Jan-1999", "20-Aug-2000", 2, 15332])
    check_temple(temples_dict, "Cardston Alberta Temple", ["Cardston Alberta Temple", "27-Jun-1913", "9-Nov-1913", "26-Aug-1923", 5, 88562])
    check_temple(temples_dict, "Cebu Philippines Temple", ["Cebu Philippines Temple", "18-Apr-2006", "14-Nov-2007", "13-Jun-2010", 2, 29556])
    check_temple(temples_dict, "Cedar City Utah Temple", ["Cedar City Utah Temple", "6-Apr-2013", "8-Aug-2015", "10-Dec-2017", 3, 42657])
    check_temple(temples_dict, "Chicago Illinois Temple", ["Chicago Illinois Temple", "1-Apr-1981", "13-Aug-1983", "9-Aug-1985", 3, 37062])
    check_temple(temples_dict, "Ciudad Juarez Mexico Temple", ["Ciudad Juarez Mexico Temple", "7-May-1998", "9-Jan-1999", "26-Feb-2000", 2, 10700])
    check_temple(temples_dict, "Cochabamba Bolivia Temple", ["Cochabamba Bolivia Temple", "13-Jan-1995", "10-Nov-1996", "30-Apr-2000", 3, 33302])
    check_temple(temples_dict, "Colonia Juarez Chihuahua Mexico Temple", ["Colonia Juarez Chihuahua Mexico Temple", "4-Oct-1997", "7-Mar-1998", "6-Mar-1999", 1, 6800])
    check_temple(temples_dict, "Columbia River Washington Temple", ["Columbia River Washington Temple", "2-Apr-2000", "28-Oct-2000", "18-Nov-2001", 2, 16880])
    check_temple(temples_dict, "Columbia South Carolina Temple", ["Columbia South Carolina Temple", "11-Sep-1998", "5-Dec-1998", "16-Oct-1999", 2, 10700])
    check_temple(temples_dict, "Columbus Ohio Temple", ["Columbus Ohio Temple", "25-Apr-1998", "12-Sep-1998", "4-Sep-1999", 2, 10700])
    check_temple(temples_dict, "Concepcion Chile Temple", ["Concepcion Chile Temple", "3-Oct-2009", "17-Oct-2015", "28-Oct-2018", 2, 23095])
    check_temple(temples_dict, "Copenhagen Denmark Temple", ["Copenhagen Denmark Temple", "17-Mar-1999", "24-Apr-1999", "23-May-2004", 2, 25000])
    check_temple(temples_dict, "Cordoba Argentina Temple", ["Cordoba Argentina Temple", "4-Oct-2008", "30-Oct-2010", "17-May-2015", 2, 34369])
    check_temple(temples_dict, "Curitiba Brazil Temple", ["Curitiba Brazil Temple", "23-Aug-2002", "10-Mar-2005", "1-Jun-2008", 2, 27850])
    check_temple(temples_dict, "Dallas Texas Temple", ["Dallas Texas Temple", "1-Apr-1981", "22-Jan-1983", "19-Oct-1984", 4, 44207])
    check_temple(temples_dict, "Denver Colorado Temple", ["Denver Colorado Temple", "31-Mar-1982", "19-May-1984", "24-Oct-1986", 5, 29117])
    check_temple(temples_dict, "Detroit Michigan Temple", ["Detroit Michigan Temple", "10-Aug-1998", "10-Oct-1998", "23-Oct-1999", 2, 10700])
    check_temple(temples_dict, "Draper Utah Temple", ["Draper Utah Temple", "2-Oct-2004", "5-Aug-2006", "20-Mar-2009", 5, 58300])
    check_temple(temples_dict, "Durban South Africa Temple", ["Durban South Africa Temple", "1-Oct-2011", "9-Apr-2016", "16-Feb-2020", 1, 19860])
    check_temple(temples_dict, "Edmonton Alberta Temple", ["Edmonton Alberta Temple", "11-Aug-1998", "27-Feb-1999", "11-Dec-1999", 2, 10700])
    check_temple(temples_dict, "Fort Collins Colorado Temple", ["Fort Collins Colorado Temple", "2-Apr-2011", "24-Aug-2013", "16-Oct-2016", 3, 42000])
    check_temple(temples_dict, "Fort Lauderdale Florida Temple", ["Fort Lauderdale Florida Temple", "3-Oct-2009", "18-Jun-2011", "4-May-2014", 3, 30500])
    check_temple(temples_dict, "Fortaleza Brazil Temple", ["Fortaleza Brazil Temple", "3-Oct-2009", "15-Nov-2011", "2-Jun-2019", 2, 36000])
    check_temple(temples_dict, "Frankfurt Germany Temple", ["Frankfurt Germany Temple", "1-Apr-1981", "1-Jul-1985", "28-Aug-1987", 4, 32895])
    check_temple(temples_dict, "Freiberg Germany Temple", ["Freiberg Germany Temple", "9-Oct-1982", "23-Apr-1983", "29-Jun-1985", 2, 21500])
    check_temple(temples_dict, "Fresno California Temple", ["Fresno California Temple", "8-Jan-1999", "20-Mar-1999", "9-Apr-2000", 2, 10700])
    check_temple(temples_dict, "Fukuoka Japan Temple", ["Fukuoka Japan Temple", "7-May-1998", "20-Mar-1999", "11-Jun-2000", 2, 10700])
    check_temple(temples_dict, "Gilbert Arizona Temple", ["Gilbert Arizona Temple", "26-Apr-2008", "13-Nov-2010", "2-Mar-2014", 7, 85326])
    check_temple(temples_dict, "Guadalajara Mexico Temple", ["Guadalajara Mexico Temple", "14-Apr-1999", "12-Jun-1999", "29-Apr-2001", 2, 10700])
    check_temple(temples_dict, "Guatemala City Guatemala Temple", ["Guatemala City Guatemala Temple", "1-Apr-1981", "12-Sep-1982", "14-Dec-1984", 3, 11610])
    check_temple(temples_dict, "Guayaquil Ecuador Temple", ["Guayaquil Ecuador Temple", "31-Mar-1982", "10-Aug-1996", "1-Aug-1999", 3, 45000])
    check_temple(temples_dict, "Halifax Nova Scotia Temple", ["Halifax Nova Scotia Temple", "7-May-1998", "12-Oct-1998", "14-Nov-1999", 2, 10700])
    check_temple(temples_dict, "Hamilton New Zealand Temple", ["Hamilton New Zealand Temple", "17-Feb-1955", "21-Dec-1955", "20-Apr-1958", 5, 44212])
    check_temple(temples_dict, "Hartford Connecticut Temple", ["Hartford Connecticut Temple", "2-Oct-2010", "17-Aug-2013", "20-Nov-2016", 2, 32246])
    check_temple(temples_dict, "Helsinki Finland Temple", ["Helsinki Finland Temple", "2-Apr-2000", "29-Mar-2003", "22-Oct-2006", 2, 16350])
    check_temple(temples_dict, "Hermosillo Sonora Mexico Temple", ["Hermosillo Sonora Mexico Temple", "20-Jul-1998", "5-Dec-1998", "27-Feb-2000", 2, 10769])
    check_temple(temples_dict, "Hong Kong China Temple", ["Hong Kong China Temple", "3-Oct-1992", "22-Jan-1994", "26-May-1996", 2, 51921])
    check_temple(temples_dict, "Houston Texas Temple", ["Houston Texas Temple", "30-Sep-1997", "13-Jun-1998", "26-Aug-2000", 3, 33970])
    check_temple(temples_dict, "Idaho Falls Idaho Temple", ["Idaho Falls Idaho Temple", "3-Mar-1937", "19-Dec-1939", "23-Sep-1945", 7, 85624])
    check_temple(temples_dict, "Indianapolis Indiana Temple", ["Indianapolis Indiana Temple", "2-Oct-2010", "29-Sep-2012", "23-Aug-2015", 2, 34000])
    check_temple(temples_dict, "Johannesburg South Africa Temple", ["Johannesburg South Africa Temple", "1-Apr-1981", "27-Nov-1982", "24-Aug-1985", 3, 19184])
    check_temple(temples_dict, "Jordan River Utah Temple", ["Jordan River Utah Temple", "3-Feb-1978", "9-Jun-1979", "16-Nov-1981", 16, 148236])
    check_temple(temples_dict, "Kansas City Missouri Temple", ["Kansas City Missouri Temple", "4-Oct-2008", "8-May-2010", "6-May-2012", 3, 32000])
    check_temple(temples_dict, "Kinshasa Democratic Republic of the Congo Temple", ["Kinshasa Democratic Republic of the Congo Temple", "1-Oct-2011", "12-Feb-2016", "14-Apr-2019", 1, 12000])
    check_temple(temples_dict, "Kona Hawaii Temple", ["Kona Hawaii Temple", "7-May-1998", "13-Mar-1999", "23-Jan-2000", 2, 10700])
    check_temple(temples_dict, "Kyiv Ukraine Temple", ["Kyiv Ukraine Temple", "20-Jul-1998", "23-Jun-2007", "29-Aug-2010", 2, 22184])
    check_temple(temples_dict, "Laie Hawaii Temple", ["Laie Hawaii Temple", "3-Oct-1915", "8-Feb-1916", "27-Nov-1919", 5, 42100])
    check_temple(temples_dict, "Las Vegas Nevada Temple", ["Las Vegas Nevada Temple", "7-Apr-1984", "30-Nov-1985", "16-Dec-1989", 6, 80350])
    check_temple(temples_dict, "Lima Peru Temple", ["Lima Peru Temple", "1-Apr-1981", "11-Sep-1982", "10-Jan-1986", 3, 9600])
    check_temple(temples_dict, "Lisbon Portugal Temple", ["Lisbon Portugal Temple", "2-Oct-2010", "5-Dec-2015", "15-Sep-2019", 1, 23730])
    check_temple(temples_dict, "Logan Utah Temple", ["Logan Utah Temple", "6-Oct-1876", "18-May-1877", "17-May-1884", 11, 119619])
    check_temple(temples_dict, "London England Temple", ["London England Temple", "10-Aug-1953", "27-Aug-1955", "7-Sep-1958", 8, 42652])
    check_temple(temples_dict, "Los Angeles California Temple", ["Los Angeles California Temple", "6-Mar-1937", "22-Sep-1951", "11-Mar-1956", 10, 190614])
    check_temple(temples_dict, "Louisville Kentucky Temple", ["Louisville Kentucky Temple", "17-Mar-1999", "29-May-1999", "19-Mar-2000", 2, 10700])
    check_temple(temples_dict, "Lubbock Texas Temple", ["Lubbock Texas Temple", "2-Apr-2000", "4-Nov-2000", "21-Apr-2002", 2, 16498])
    check_temple(temples_dict, "Madrid Spain Temple", ["Madrid Spain Temple", "4-Apr-1993", "11-Jun-1996", "19-Mar-1999", 4, 45800])
    check_temple(temples_dict, "Manaus Brazil Temple", ["Manaus Brazil Temple", "23-May-2007", "20-Jun-2008", "10-Jun-2012", 2, 32032])
    check_temple(temples_dict, "Manhattan New York Temple", ["Manhattan New York Temple", "7-Aug-2002", "23-Sep-2002", "13-Jun-2004", 2, 20630])
    check_temple(temples_dict, "Manila Philippines Temple", ["Manila Philippines Temple", "1-Apr-1981", "25-Aug-1982", "25-Sep-1984", 3, 26683])
    check_temple(temples_dict, "Manti Utah Temple", ["Manti Utah Temple", "25-Jun-1875", "25-Apr-1877", "21-May-1888", 8, 74792])
    check_temple(temples_dict, "Medford Oregon Temple", ["Medford Oregon Temple", "15-Mar-1999", "20-May-1999", "16-Apr-2000", 2, 10700])
    check_temple(temples_dict, "Melbourne Australia Temple", ["Melbourne Australia Temple", "30-Oct-1998", "20-Mar-1999", "16-Jun-2000", 2, 10700])
    check_temple(temples_dict, "Memphis Tennessee Temple", ["Memphis Tennessee Temple", "17-Sep-1998", "16-Jan-1999", "23-Apr-2000", 2, 10890])
    check_temple(temples_dict, "Merida Mexico Temple", ["Merida Mexico Temple", "25-Sep-1998", "16-Jan-1999", "8-Jul-2000", 2, 10700])
    check_temple(temples_dict, "Meridian Idaho Temple", ["Meridian Idaho Temple", "2-Apr-2011", "23-Aug-2014", "19-Nov-2017", 5, 67331])
    check_temple(temples_dict, "Mesa Arizona Temple", ["Mesa Arizona Temple", "3-Oct-1919", "25-Apr-1922", "23-Oct-1927", 6, 113916])
    check_temple(temples_dict, "Mexico City Mexico Temple", ["Mexico City Mexico Temple", "3-Apr-1976", "25-Nov-1979", "2-Dec-1983", 11, 116642])
    check_temple(temples_dict, "Monterrey Mexico Temple", ["Monterrey Mexico Temple", "21-Dec-1995", "4-Nov-2000", "28-Apr-2002", 2, 16498])
    check_temple(temples_dict, "Montevideo Uruguay Temple", ["Montevideo Uruguay Temple", "2-Nov-1998", "27-Apr-1999", "18-Mar-2001", 2, 10700])
    check_temple(temples_dict, "Monticello Utah Temple", ["Monticello Utah Temple", "4-Oct-1997", "17-Nov-1997", "26-Jul-1998", 2, 11225])
    check_temple(temples_dict, "Montreal Quebec Temple", ["Montreal Quebec Temple", "6-Aug-1998", "9-Apr-1999", "4-Jun-2000", 2, 11550])
    check_temple(temples_dict, "Mount Timpanogos Utah Temple", ["Mount Timpanogos Utah Temple", "3-Oct-1992", "9-Oct-1993", "13-Oct-1996", 8, 107240])
    check_temple(temples_dict, "Nashville Tennessee Temple", ["Nashville Tennessee Temple", "9-Nov-1994", "13-Mar-1999", "21-May-2000", 2, 10700])
    check_temple(temples_dict, "Nauvoo Illinois Temple", ["Nauvoo Illinois Temple", "4-Apr-1999", "24-Oct-1999", "27-Jun-2002", 6, 54000])
    check_temple(temples_dict, "Newport Beach California Temple", ["Newport Beach California Temple", "21-Apr-2001", "15-Aug-2003", "28-Aug-2005", 3, 17800])
    check_temple(temples_dict, "Nuku'alofa Tonga Temple", ["Nuku'alofa Tonga Temple", "2-Apr-1980", "18-Feb-1981", "9-Aug-1983", 3, 21184])
    check_temple(temples_dict, "Oakland California Temple", ["Oakland California Temple", "23-Jan-1961", "26-May-1962", "17-Nov-1964", 7, 80157])
    check_temple(temples_dict, "Oaxaca Mexico Temple", ["Oaxaca Mexico Temple", "23-Feb-1999", "13-Mar-1999", "11-Mar-2000", 2, 10700])
    check_temple(temples_dict, "Ogden Utah Temple", ["Ogden Utah Temple", "24-Aug-1967", "8-Sep-1969", "18-Jan-1972", 9, 112232])
    check_temple(temples_dict, "Oklahoma City Oklahoma Temple", ["Oklahoma City Oklahoma Temple", "14-Mar-1999", "3-Jul-1999", "30-Jul-2000", 2, 10890])
    check_temple(temples_dict, "Oquirrh Mountain Utah Temple", ["Oquirrh Mountain Utah Temple", "1-Oct-2005", "16-Dec-2006", "21-Aug-2009", 7, 60000])
    check_temple(temples_dict, "Orlando Florida Temple", ["Orlando Florida Temple", "17-Feb-1990", "20-Jun-1992", "9-Oct-1994", 5, 70000])
    check_temple(temples_dict, "Palmyra New York Temple", ["Palmyra New York Temple", "21-Feb-1999", "25-May-1999", "6-Apr-2000", 2, 10900])
    check_temple(temples_dict, "Panama City Panama Temple", ["Panama City Panama Temple", "23-Aug-2002", "30-Oct-2005", "10-Aug-2008", 2, 18943])
    check_temple(temples_dict, "Papeete Tahiti Temple", ["Papeete Tahiti Temple", "2-Apr-1980", "13-Feb-1981", "27-Oct-1983", 2, 12150])
    check_temple(temples_dict, "Paris France Temple", ["Paris France Temple", "1-Oct-2011", "24-Aug-2012", "21-May-2017", 3, 44175])
    check_temple(temples_dict, "Payson Utah Temple", ["Payson Utah Temple", "25-Jan-2010", "8-Oct-2011", "7-Jun-2015", 7, 96630])
    check_temple(temples_dict, "Perth Australia Temple", ["Perth Australia Temple", "11-Jun-1999", "20-Nov-1999", "20-May-2001", 2, 10700])
    check_temple(temples_dict, "Philadelphia Pennsylvania Temple", ["Philadelphia Pennsylvania Temple", "4-Oct-2008", "17-Sep-2011", "18-Sep-2016", 4, 61466])
    check_temple(temples_dict, "Phoenix Arizona Temple", ["Phoenix Arizona Temple", "24-May-2008", "4-Jun-2011", "16-Nov-2014", 4, 64870])
    check_temple(temples_dict, "Pocatello Idaho Temple", ["Pocatello Idaho Temple", "2-Apr-2017", "16-Mar-2019", "7-Nov-2021", 4, 71125])
    check_temple(temples_dict, "Port-au-Prince Haiti Temple", ["Port-au-Prince Haiti Temple", "5-Apr-2015", "28-Oct-2017", "1-Sep-2019", 1, 10396])
    check_temple(temples_dict, "Portland Oregon Temple", ["Portland Oregon Temple", "7-Apr-1984", "20-Sep-1986", "19-Aug-1989", 14, 80500])
    check_temple(temples_dict, "Porto Alegre Brazil Temple", ["Porto Alegre Brazil Temple", "30-Sep-1997", "2-May-1998", "17-Dec-2000", 2, 10700])
    check_temple(temples_dict, "Praia Cape Verde Temple", ["Praia Cape Verde Temple", "7-Oct-2018", "4-May-2019", "19-Jun-2022", 1, 8759])
    check_temple(temples_dict, "Preston England Temple", ["Preston England Temple", "19-Oct-1992", "12-Jun-1994", "7-Jun-1998", 4, 69630])
    check_temple(temples_dict, "Provo City Center Utah Temple", ["Provo City Center Utah Temple", "1-Oct-2011", "12-May-2012", "20-Mar-2016", 5, 85084])
    check_temple(temples_dict, "Provo Utah Temple", ["Provo Utah Temple", "14-Aug-1967", "15-Sep-1969", "9-Feb-1972", 12, 130825])
    check_temple(temples_dict, "Quetzaltenango Guatemala Temple", ["Quetzaltenango Guatemala Temple", "16-Dec-2006", "14-Mar-2009", "11-Dec-2011", 2, 21085])
    check_temple(temples_dict, "Quito Ecuador Temple", ["Quito Ecuador Temple", "3-Apr-2016", "11-May-2019", "20-Nov-2022", 0, 0])
    check_temple(temples_dict, "Raleigh North Carolina Temple", ["Raleigh North Carolina Temple", "3-Sep-1998", "6-Feb-1999", "18-Dec-1999", 2, 12864])
    check_temple(temples_dict, "Recife Brazil Temple", ["Recife Brazil Temple", "13-Jan-1995", "11-Nov-1996", "15-Dec-2000", 3, 37200])
    check_temple(temples_dict, "Redlands California Temple", ["Redlands California Temple", "21-Apr-2001", "1-Dec-2001", "14-Sep-2003", 3, 17300])
    check_temple(temples_dict, "Regina Saskatchewan Temple", ["Regina Saskatchewan Temple", "3-Aug-1998", "14-Nov-1998", "14-Nov-1999", 2, 10700])
    check_temple(temples_dict, "Reno Nevada Temple", ["Reno Nevada Temple", "12-Apr-1999", "24-Jul-1999", "23-Apr-2000", 2, 10700])
    check_temple(temples_dict, "Rexburg Idaho Temple", ["Rexburg Idaho Temple", "12-Dec-2003", "30-Jul-2005", "10-Feb-2008", 5, 57504])
    check_temple(temples_dict, "Rio de Janeiro Brazil Temple", ["Rio de Janeiro Brazil Temple", "6-Apr-2013", "4-Mar-2017", "8-May-2022", 0, 29966])
    check_temple(temples_dict, "Rome Italy Temple", ["Rome Italy Temple", "4-Oct-2008", "23-Oct-2010", "10-Mar-2019", 3, 41010])
    check_temple(temples_dict, "Sacramento California Temple", ["Sacramento California Temple", "21-Apr-2001", "22-Aug-2004", "3-Sep-2006", 4, 19500])
    check_temple(temples_dict, "Salt Lake City Utah Temple", ["Salt Lake City Utah Temple", "28-Jul-1847", "14-Feb-1853", "6-Apr-1893", 23, 253000])
    check_temple(temples_dict, "San Antonio Texas Temple", ["San Antonio Texas Temple", "24-Jun-2001", "29-Mar-2003", "22-May-2005", 2, 16800])
    check_temple(temples_dict, "San Diego California Temple", ["San Diego California Temple", "7-Apr-1984", "27-Feb-1988", "25-Apr-1993", 8, 72000])
    check_temple(temples_dict, "San Jose Costa Rica Temple", ["San Jose Costa Rica Temple", "17-Mar-1999", "24-Apr-1999", "4-Jun-2000", 2, 10700])
    check_temple(temples_dict, "San Salvador El Salvador Temple", ["San Salvador El Salvador Temple", "18-Nov-2007", "20-Sep-2008", "21-Aug-2011", 2, 27986])
    check_temple(temples_dict, "Santiago Chile Temple", ["Santiago Chile Temple", "2-Apr-1980", "30-May-1981", "15-Sep-1983", 3, 20831])
    check_temple(temples_dict, "Santo Domingo Dominican Republic Temple", ["Santo Domingo Dominican Republic Temple", "16-Nov-1993", "18-Aug-1996", "17-Sep-2000", 4, 67000])
    check_temple(temples_dict, "Sao Paulo Brazil Temple", ["Sao Paulo Brazil Temple", "1-Mar-1975", "20-Mar-1976", "30-Oct-1978", 4, 59246])
    check_temple(temples_dict, "Sapporo Japan Temple", ["Sapporo Japan Temple", "3-Oct-2009", "22-Oct-2011", "21-Aug-2016", 3, 48480])
    check_temple(temples_dict, "Seattle Washington Temple", ["Seattle Washington Temple", "15-Nov-1975", "27-May-1978", "17-Nov-1980", 13, 110000])
    check_temple(temples_dict, "Seoul Korea Temple", ["Seoul Korea Temple", "1-Apr-1981", "9-May-1983", "14-Dec-1985", 3, 28057])
    check_temple(temples_dict, "Snowflake Arizona Temple", ["Snowflake Arizona Temple", "2-Apr-2000", "23-Sep-2000", "3-Mar-2002", 2, 18621])
    check_temple(temples_dict, "Spokane Washington Temple", ["Spokane Washington Temple", "13-Aug-1998", "10-Oct-1998", "21-Aug-1999", 2, 10700])
    check_temple(temples_dict, "St. George Utah Temple", ["St. George Utah Temple", "31-Jan-1871", "9-Nov-1871", "6-Apr-1877", 18, 142000])
    check_temple(temples_dict, "St. Louis Missouri Temple", ["St. Louis Missouri Temple", "29-Dec-1990", "30-Oct-1993", "1-Jun-1997", 4, 58749])
    check_temple(temples_dict, "St. Paul Minnesota Temple", ["St. Paul Minnesota Temple", "29-Jul-1998", "26-Sep-1998", "9-Jan-2000", 2, 10700])
    check_temple(temples_dict, "Star Valley Wyoming Temple", ["Star Valley Wyoming Temple", "1-Oct-2011", "25-Apr-2015", "30-Oct-2016", 1, 18609])
    check_temple(temples_dict, "Stockholm Sweden Temple", ["Stockholm Sweden Temple", "1-Apr-1981", "17-Mar-1984", "2-Jul-1985", 3, 16366])
    check_temple(temples_dict, "Suva Fiji Temple", ["Suva Fiji Temple", "7-May-1998", "8-May-1999", "18-Jun-2000", 2, 12755])
    check_temple(temples_dict, "Sydney Australia Temple", ["Sydney Australia Temple", "2-Apr-1980", "13-Aug-1982", "20-Sep-1984", 3, 30677])
    check_temple(temples_dict, "Taipei Taiwan Temple", ["Taipei Taiwan Temple", "31-Mar-1982", "27-Aug-1982", "17-Nov-1984", 3, 9945])
    check_temple(temples_dict, "Tampico Mexico Temple", ["Tampico Mexico Temple", "8-Jul-1998", "28-Nov-1998", "20-May-2000", 2, 10700])
    check_temple(temples_dict, "Tegucigalpa Honduras Temple", ["Tegucigalpa Honduras Temple", "9-Jun-2006", "12-Sep-2009", "17-Mar-2013", 2, 28254])
    check_temple(temples_dict, "The Gila Valley Arizona Temple", ["The Gila Valley Arizona Temple", "26-Apr-2008", "14-Feb-2009", "23-May-2010", 2, 18561])
    check_temple(temples_dict, "The Hague Netherlands Temple", ["The Hague Netherlands Temple", "16-Aug-1999", "26-Aug-2000", "8-Sep-2002", 2, 10500])
    check_temple(temples_dict, "Tijuana Mexico Temple", ["Tijuana Mexico Temple", "2-Oct-2010", "18-Aug-2012", "13-Dec-2015", 2, 33367])
    check_temple(temples_dict, "Tokyo Japan Temple", ["Tokyo Japan Temple", "9-Aug-1975", "10-Apr-1978", "27-Oct-1980", 5, 52590])
    check_temple(temples_dict, "Toronto Ontario Temple", ["Toronto Ontario Temple", "7-Apr-1984", "10-Oct-1987", "25-Aug-1990", 6, 57982])
    check_temple(temples_dict, "Trujillo Peru Temple", ["Trujillo Peru Temple", "13-Dec-2008", "14-Sep-2011", "21-Jun-2015", 2, 28200])
    check_temple(temples_dict, "Tucson Arizona Temple", ["Tucson Arizona Temple", "6-Oct-2012", "17-Oct-2015", "13-Aug-2017", 2, 38216])
    check_temple(temples_dict, "Tuxtla Gutierrez Mexico Temple", ["Tuxtla Gutierrez Mexico Temple", "25-Feb-1999", "20-Mar-1999", "12-Mar-2000", 2, 10700])
    check_temple(temples_dict, "Twin Falls Idaho Temple", ["Twin Falls Idaho Temple", "2-Oct-2004", "15-Apr-2006", "24-Aug-2008", 3, 31245])
    check_temple(temples_dict, "Vancouver British Columbia Temple", ["Vancouver British Columbia Temple", "25-May-2006", "4-Aug-2007", "2-May-2010", 2, 28165])
    check_temple(temples_dict, "Veracruz Mexico Temple", ["Veracruz Mexico Temple", "14-Apr-1999", "29-May-1999", "9-Jul-2000", 2, 10700])
    check_temple(temples_dict, "Vernal Utah Temple", ["Vernal Utah Temple", "13-Feb-1994", "13-May-1995", "2-Nov-1997", 3, 38771])
    check_temple(temples_dict, "Villahermosa Mexico Temple", ["Villahermosa Mexico Temple", "30-Oct-1998", "9-Jan-1999", "21-May-2000", 2, 10700])
    check_temple(temples_dict, "Washington D.C. Temple", ["Washington D.C. Temple", "15-Nov-1968", "7-Dec-1968", "19-Nov-1974", 10, 156558])
    check_temple(temples_dict, "Winnipeg Manitoba Temple", ["Winnipeg Manitoba Temple", "2-Apr-2011", "3-Dec-2016", "31-Oct-2021", 1, 16100])
    check_temple(temples_dict, "Winter Quarters Nebraska Temple", ["Winter Quarters Nebraska Temple", "14-Jun-1999", "28-Nov-1999", "22-Apr-2001", 2, 16000])
    check_temple(temples_dict, "Yigo Guam Temple", ["Yigo Guam Temple", "7-Oct-2018", "4-May-2019", "22-May-2022", 1, 6861])

def check_president(presidents_dict, president_name, expected):
    """Verify that the data for one president stored in the
    president dictionary is correct.

    Parameters
        presidents_dict: a dictionary that contains church presidents data
        president_name: the name of the president that this
            function will verify
        expected: the data that should be in the presidents
            dictionary for the president_name
    Return: nothing
    """
    assert president_name in presidents_dict, \
        f'"{president_name}" is missing from the presidents dictionary.'
    actual = presidents_dict[president_name]

    # Verify that the president's birthdate is correct.
    act_birthdate = actual[BIRTHDATE_INDEX]
    exp_birthdate = expected[BIRTHDATE_INDEX]
    assert act_birthdate == exp_birthdate, \
            f'wrong birthdate for "{president_name}": ' \
            f'expected {exp_birthdate} but found {act_birthdate}'

    # Verify that the president's ordination date is correct.
    act_ordination = actual[ORDINATION_INDEX]
    exp_ordination = expected[ORDINATION_INDEX]
    assert act_ordination == exp_ordination, \
            f'wrong ordination date for "{president_name}": ' \
            f'expected {exp_ordination} but found {act_ordination}'

    # Verify that the president's death date is correct.
    act_death = actual[DEATH_INDEX]
    exp_death = expected[DEATH_INDEX]
    assert act_death == exp_death, \
            f'wrong deathdate for "{president_name}": ' \
            f'expected {exp_death} but found {act_death}'

    # Verify that the number of announcements is correct.
    act_announcements = int(actual[PRESIDENT_TEMPLE_ANNOUNCEMENTS_INDEX])
    exp_announcements = int(expected[PRESIDENT_TEMPLE_ANNOUNCEMENTS_INDEX])
    assert act_announcements == exp_announcements, \
            f'wrong number of announcements for "{president_name}": ' \
            f'expected {exp_announcements} but found {act_announcements}'

    # Verify that the number of groundbreakings is correct.
    act_groundbreakings = int(actual[PRESIDENT_TEMPLE_GROUNDBREAKINGS_INDEX])
    exp_groundbreakings = int(expected[PRESIDENT_TEMPLE_GROUNDBREAKINGS_INDEX])
    assert act_groundbreakings == exp_groundbreakings, \
            f'wrong number of groundbreakings for "{president_name}": ' \
            f'expected {exp_groundbreakings} but found {act_groundbreakings}'

    # Verify that the number of dedications is correct.
    act_dedications = int(actual[PRESIDENT_TEMPLE_DEDICATIONS_INDEX])
    exp_dedications = int(expected[PRESIDENT_TEMPLE_DEDICATIONS_INDEX])
    assert act_dedications == exp_dedications, \
            f'wrong number of dedications for "{president_name}": ' \
            f'expected {exp_dedications} but found {act_dedications}'



def check_temple(temples_dict, temple_name, expected):
    """Verify that the data for one temple stored in the
    temples dictionary is correct.

    Parameters
        temples_dict: a dictionary that contains temple data
        temple_name: the name of the temple that this
            function will verify
        expected: the data that should be in the temples dictionary 
            for the temple_name
    Return: nothing
    """
    assert temple_name in temples_dict, \
        f'"{temple_name}" is missing from the temples dictionary.'
    actual = temples_dict[temple_name]

    # Verify that the temple's announced date is correct.
    act_announced = actual[TEMPLE_ANNOUNCED_INDEX]
    exp_announced = expected[TEMPLE_ANNOUNCED_INDEX]
    assert act_announced == exp_announced, \
            f'wrong announced date for "{temple_name}": ' \
            f'expected {exp_announced} but found {act_announced}'

    # Verify that the temple's groundbreaking date is correct.
    act_groundbreaking = actual[TEMPLE_GROUNDBREAKING_INDEX]
    exp_groundbreaking = expected[TEMPLE_GROUNDBREAKING_INDEX]
    assert act_groundbreaking == exp_groundbreaking, \
            f'wrong groundbreaking date for "{temple_name}": ' \
            f'expected {exp_groundbreaking} but found {act_groundbreaking}'

    # Verify that the temple's dedication date is correct.
    act_dedication = actual[TEMPLE_DEDICATION_INDEX]
    exp_dedication = expected[TEMPLE_DEDICATION_INDEX]
    assert act_dedication == exp_dedication, \
            f'wrong dedication date for "{temple_name}": ' \
            f'expected {exp_dedication} but found {act_dedication}'

    # Verify that the number of sealing rooms is correct.
    act_sealing = float(actual[TEMPLE_NUMBER_SEALING_ROOMS_INDEX])
    exp_sealing = float(expected[TEMPLE_NUMBER_SEALING_ROOMS_INDEX])
    assert act_sealing == exp_sealing, \
            f'wrong number of sealing rooms for "{temple_name}": ' \
            f'expected {exp_sealing} but found {act_sealing}'

    # Verify that the temple's square footage is correct.
    act_sqft = float(actual[TEMPLE_SQFT_INDEX])
    exp_sqft = float(expected[TEMPLE_SQFT_INDEX])
    assert act_sqft == exp_sqft, \
            f'wrong square footage for "{temple_name}": ' \
            f'expected {exp_sqft} but found {act_sqft}'


def test_days_between():
    """Verify that the days_between function works correctly.
    Parameters: none
    Return: nothing
    """

    current_date = datetime.now().strftime("%d-%b-%Y")
    temples_dict = read_dict("temples.csv", TEMPLE_NAME_INDEX)

    for temple in temples_dict:
        temple_name = temples_dict[temple]
        announced = temple_name[TEMPLE_ANNOUNCED_INDEX]
        groundbreaking = temple_name[TEMPLE_GROUNDBREAKING_INDEX]
        dedication = temple_name[TEMPLE_DEDICATION_INDEX]

        # verify that the nuumber of days between current and dedication is correct
        assert days_between(current_date,dedication) == \
                abs(((datetime.strptime(dedication, "%d-%b-%Y"))-(datetime.strptime(current_date, "%d-%b-%Y"))).days)  
        
        # verify that the nuumber of days between groundbreaking and announcement is correct
        assert days_between(announced,groundbreaking) == \
                abs(((datetime.strptime(groundbreaking, "%d-%b-%Y"))-(datetime.strptime(announced, "%d-%b-%Y"))).days)
        
        # verify that the nuumber of days between dedication and groundbreaking is correct
        assert days_between(groundbreaking,dedication) == \
                abs(((datetime.strptime(dedication, "%d-%b-%Y"))-(datetime.strptime(groundbreaking, "%d-%b-%Y"))).days)
        
        # verify that the nuumber of days between dedication and announcement is correct
        assert days_between(announced,dedication) == \
                abs(((datetime.strptime(dedication, "%d-%b-%Y"))-(datetime.strptime(announced, "%d-%b-%Y"))).days)
    


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])




