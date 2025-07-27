import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_hacker_news():
    base_url = "https://news.ycombinator.com/news"
    all_articles = []
    
    # Hacker News는 페이지당 약 30개의 기사를 보여줍니다.
    # 100개 이상의 기사를 얻기 위해 4페이지까지 스크래핑합니다.
    for page_num in range(1, 5): 
        url = f"{base_url}?p={page_num}"
        print(f"Scraping {url}...")
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # HTTP 오류가 발생하면 예외 발생
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            continue # 다음 페이지로 넘어감

        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 각 기사 항목을 찾습니다.
        # Hacker News HTML 구조에 따라 'athing' 클래스를 가진 tr 태그가 기사 하나를 나타냅니다.
        articles = soup.find_all('tr', class_='athing')
        
        for article in articles:
            title_tag = article.find('span', class_='titleline')
            if title_tag:
                title = title_tag.a.get_text(strip=True)
                link = title_tag.a['href']
            else:
                title = "No Title Found"
                link = "No Link Found"

            # 기사 바로 아래에 있는 'subtext' 클래스의 tr 태그를 찾아서 점수, 작성자, 시간 정보를 가져옵니다.
            # athing tr 다음에 subtext tr이 나옵니다.
            subtext_row = article.find_next_sibling('tr')
            
            score = "N/A"
            author = "N/A"
            comments_link = "N/A"

            if subtext_row:
                score_span = subtext_row.find('span', class_='score')
                if score_span:
                    score = score_span.get_text(strip=True)
                
                user_link = subtext_row.find('a', class_='hnuser')
                if user_link:
                    author = user_link.get_text(strip=True)
                
                age_span = subtext_row.find('span', class_='age')
                if age_span:
                    time_tag = age_span.find('a')
                    if time_tag:
                        time = time_tag.get_text(strip=True)

                # 댓글 링크 찾기 (가장 마지막 a 태그)
                # 댓글 수가 0일 경우 'discuss'만 있고 숫자가 없을 수 있습니다.
                comments_tags = subtext_row.find_all('a')
                if comments_tags:
                    for tag in comments_tags:
                        if 'comments' in tag.get_text(strip=True).lower() or 'discuss' in tag.get_text(strip=True).lower():
                            comments_link = tag['href']
                            break

            all_articles.append({
                'Rank': len(all_articles) + 1,  # 순위는 스크래핑된 순서대로 부여합니다.
                'Title': title,
                'Link': link,
                'Score': score,
                'Author': author,
                'Comments Link': f"https://news.ycombinator.com/{comments_link}" if comments_link != "N/A" else "N/A"
            })
            
            # 100개 기사가 모이면 중단
            if len(all_articles) >= 100:
                break
        
        if len(all_articles) >= 100:
            print("100 articles scraped. Stopping.")
            break

    return all_articles[:100] # 혹시 100개를 초과해서 가져왔을 경우 딱 100개만 반환

if __name__ == "__main__":
    articles_data = scrape_hacker_news()

    if articles_data:
        df = pd.DataFrame(articles_data)
        
        # 엑셀 파일로 저장
        excel_file_name = "ycombinator_news_top100.xlsx"
        try:
            df.to_excel(excel_file_name, index=False)
            print(f"\nSuccessfully saved {len(articles_data)} articles to '{excel_file_name}'")
        except Exception as e:
            print(f"Error saving to Excel: {e}")
    else:
        print("No articles were scraped.")