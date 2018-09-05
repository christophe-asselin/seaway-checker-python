import bs4
import requests


def main():
    print_header()
    html = get_html_from_web()
    status = get_status_from_html(html)
    print(status)


def print_header():
    """
    Print a header for the app
    :return: None
    """
    print('-------------------------------')
    print('  SEAWAY TRAFFIC CHECKER APP')
    print('-------------------------------')
    print()


def get_html_from_web():
    """
    Get the html code from the website
    :return: html code as text
    """
    url = 'http://www.greatlakes-seaway.com/R2/jsp/mMaiBrdgStatus.jsp?language=E'
    response = requests.get(url)
    return response.text


def get_status_from_html(html):
    """
    Parse the html code to get the status of the bridge and time of future arrivals
    :param html: html code of the website as text
    :return: parsed information as text
    """
    soup = bs4.BeautifulSoup(html, "html.parser")
    status = soup.find_all('li')[1].get_text().strip()
    status = status[48:].replace('	', '')
    return status


if __name__ == '__main__':
    main()
