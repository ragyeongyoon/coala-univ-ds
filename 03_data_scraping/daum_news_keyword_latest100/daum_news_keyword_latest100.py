import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_daum_news_koala_latest():
    base_url = "https://search.daum.net/search"
    search_query = "회계"
    all_articles = []
    
    target_article_count = 100 
    
    # 1페이지부터 100개를 채울 때까지 여러 페이지를 반복
    for page_num in range(1, 11): # 최대 10페이지까지 시도
        if len(all_articles) >= target_article_count:
            print(f"Reached {target_article_count} valid articles. Stopping scrape.")
            break 

        params = {
            "w": "news",
            "DA": "PGD",
            "enc": "utf8",
            "cluster": "y",
            "cluster_page": "1", 
            "q": search_query,
            "p": page_num,
            "sort": "recency" # 최신순 정렬
        }
        
        print(f"Scraping page {page_num} for '{search_query}' (Latest News)...")
        
        try:
            raw = requests.get(base_url, params=params)
            raw.raise_for_status() 
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page_num}: {e}")
            continue

        html = BeautifulSoup(raw.text, 'html.parser')

        news_section = html.select_one("#dnsColl")

        if not news_section:
            print(f"No news section container (#dnsColl) found on page {page_num}. Ending scrape.")
            break

        articles = news_section.select("ul > li") 

        if not articles:
            print(f"No articles found within the list on page {page_num}. Ending scrape.")
            break

        for article in articles:
            title_element = article.select_one("div.item-title strong a")
            title = title_element.get_text(strip=True) if title_element else "제목 없음"
            
            # "제목 없음" 필터링
            if title == "제목 없음" or not title: 
                continue 
            
            article_url = title_element['href'] if title_element and 'href' in title_element.attrs else "URL 없음"

            media_element = article.select_one("div.c-tit-doc div.area_tit div a strong span")
            media_name = media_element.get_text(strip=True) if media_element else "신문사 없음"

            # 기사 번호 추가
            all_articles.append({
                'No.': len(all_articles) + 1, # 현재까지 수집된 기사 수 + 1
                '제목': title,
                '신문사': media_name, # 신문사 정보 추가
                'URL': article_url
            })
            
            if len(all_articles) >= target_article_count:
                print(f"Reached {target_article_count} valid articles during page {page_num}. Stopping scrape.")
                break 

        print("-" * 80) 

    return all_articles[:target_article_count]

if __name__ == "__main__":
    news_data = scrape_daum_news_koala_latest()

    if news_data:
        df = pd.DataFrame(news_data)
        
        excel_file_name = "daum_news_keyword_latest100.xlsx" # 파일 이름 변경
        try:
            df.to_excel(excel_file_name, index=False)
            print(f"\nSuccessfully saved {len(news_data)} latest valid articles to '{excel_file_name}'")
        except Exception as e:
            print(f"Error saving to Excel: {e}")
    else:
        print("No valid articles were scraped.")