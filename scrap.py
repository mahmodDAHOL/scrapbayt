from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        headless=False,
        user_data_dir=r'C:\Users\S I N O\AppData\Local\Google\Chrome\User Data\Profile',
        executable_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe')

    # Set cookies after authentication
    cookies = [
        {"name": "brID", "value": "41277344261694034932", "domain": ".example.com", "path": "/"},
        {"name": "cookieyes-consent", "value": "consentid:SlExQWtpV0lESUdEVllGbUcyTzJJMk5ZQUtNWElQZlA,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes,lastRenewedDate:1710054739000", "domain": ".example.com", "path": "/"},
        {"name": "G_ENABLED_IDPS", "value": "google", "domain": ".example.com", "path": "/"},
        {"name": "amp_6e3626", "value": "7Xu4l1Rm4x_oMIvMJKi4HI...1ikeiatct.1ikeiatct.0.0.0", "domain": ".example.com", "path": "/"},
        {"name": "cf_clearance", "value": "wBlQQxu1y5xssUl38CI.4eUA_kNr76uhcX2Wuw.wNho-1748248869-1.2.1.1-.si6CAfgmqTeE7RFglzZzvQ2Ieu.vdEs5txuE7t8.kGx4c3.38tWVeXmi37Wiwzi4w_t6MGomD3veYEDl7MbSaqs7BApKfh6Y5FVl9AMWCK9EBHZ5ZNp6xbsZ2XAsO1V0_I0FuxWup_VG.NPMJIShLXUZCJIdeiHB.if0ueu93VaRjd0XP_Gnt3lYxt.neMm_sjxByIAyPSsavasV1xEk5UNNcFq.ARf.Q01ajqozNLGA4pocI0krREXI47ISYLjVgCgZknwdpLd0YBv7G3Maz54v_cigwZe9R4N8ns79GmsDWKb9VLHbQRFXEDfMhEuh6Vrt6wtOYNqxRQcq_3l7YDaLd4oGXeJqHMA.ysnM.g", "domain": ".example.com", "path": "/"},
        {"name": "lastShowFor2FA87318455", "value": "2025-05-20", "domain": ".example.com", "path": "/"},
        {"name": "_ga", "value": "GA1.1.1613737730.1747807256", "domain": ".example.com", "path": "/"},
        {"name": "_ga_1NKPLGNKKD", "value": "GS2.1.s1748246975$o6$g1$t1748248877$j51$l0$h0$dXsp7NYx82Wb6N55Ne7CljZ2wNJ2wV6FiEw", "domain": ".example.com", "path": "/"},
        {"name": "__rtbh.uid", "value": "%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%2287318455%22%2C%22expiryDate%22%3A%222026-05-26T08%3A41%3A12.515Z%22%7D", "domain": ".example.com", "path": "/"},
        {"name": "__rtbh.lid", "value": "%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%228bEc19RmSRYCMCpE0jpc%22%2C%22expiryDate%22%3A%222026-05-26T08%3A41%3A12.515Z%22%7D", "domain": ".example.com", "path": "/"},
        {"name": "_clck", "value": "nv0xay%7C2%7Cfw8%7C1%7C1967", "domain": ".example.com", "path": "/"},
        {"name": "intercom-session-k4hq7kcu", "value": "eUxCUjl6aGRsQUFXRHhzYTFEeGt1UHZqcGpTRFBpakdCa3g2eXpjWFB4NzZaNlNqdXhFSEpVOHNTZnRxUWVjTXpHSmh0NDRVYVd0MUNxRU1TK2c5ZmFRdHNoRForc3B1Wi9GNHBFMkpCbUU9LS16QlpaOUJNK0xUWCtGckhrcnEzQUh3PT0=--f9abe48ff5367ee4ba0150088bb1f5edc19f6fc2", "domain": ".example.com", "path": "/"},
        {"name": "intercom-device-id-k4hq7kcu", "value": "1e0a36b1-4c3f-48d5-8052-4e041017f0d9", "domain": ".example.com", "path": "/"},
        {"name": "_gcl_au", "value": "1.1.1661123400.1747829170", "domain": ".example.com", "path": "/"},
        {"name": "user-prefs", "value": "locale%20xx%20lang%20en%20geo%20bg", "domain": ".example.com", "path": "/"},
        {"name": "ATL_details", "value": "SoMKLUJVzRA%3D", "domain": ".example.com", "path": "/"},
        {"name": "user_login_id0", "value": "zLXFguO2R08%3D", "domain": ".example.com", "path": "/"},
        {"name": "user_login_id1", "value": "SoMKLUJVzRA%3D", "domain": ".example.com", "path": "/"},
        {"name": "ISLOGGED0", "value": "1", "domain": ".example.com", "path": "/"},
        {"name": "SSD0", "value": "Gqfpl5%2FpItMHK%2B2RSpko4l4Wq7JyNPC3JXZH621nGzNQ2%2Fh8AVyLN9EthROiZAxD%40%40%40be2c6ff9a0a40454", "domain": ".example.com", "path": "/"},
        {"name": "MSESID0", "value": "423734971230556646107%2C87318455%2C2%2C0%2CXMYZ0Q%2C1%2C6%2C3768bba72d40f13055e341e49043b305", "domain": ".example.com", "path": "/"},
        {"name": "BSESINFO0", "value": "23%2CQ67MXR%2C423735085%2CZ7W6QO", "domain": ".example.com", "path": "/"},
        {"name": "msgCount", "value": "1", "domain": ".example.com", "path": "/"},
        {"name": "_clsk", "value": "u3wdnx%7C1748248873272%7C4%7C1%7Cj.clarity.ms%2Fcollect", "domain": ".example.com", "path": "/"},
        {"name": "UADCN", "value": "Vwy4JPrU5cG2pIq0JO0sglfUcuGvLnyEHch9cp%2FpSeA%3D%40%40%40efda58cec4e3449e", "domain": ".example.com", "path": "/"},
        {"name": "showUserCompleteProfileBanner", "value": "Yes", "domain": ".example.com", "path": "/"},
        {"name": "nav-status", "value": "%7B%22prm%22%3A%22upgrade%22%2C%22cart%22%3A0%2C%22appBnr%22%3A1%2C%22emlCnf%22%3A0%2C%22gid%22%3A%222252486%22%7D", "domain": ".example.com", "path": "/"},
        {"name": "section", "value": "emp", "domain": ".example.com", "path": "/"},
        {"name": "nav-count", "value": "0", "domain": ".example.com", "path": "/"}
    ]
    # Create a new context with extra HTTP headers
    context = browser.new_context(
        **{
            "extra_http_headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0",
                "Accept": "application/json",
                "Accept-Language": "en",
                # 'Accept-Encoding': 'gzip, deflate, br, zstd',
                "Referer": "https://www.bayt.com/en/employers/saved-search/?ssid=43859977&searchId=cogetnC5",
                "user-token": "Browser:423734971230556646107,87318455,2,0,XMYZ0Q,1,6,3768bba72d40f13055e341e49043b305&23,Q67MXR,423735085,Z7W6QO&41277344261694034932",
                "Connection": "keep-alive",
                # 'Cookie': 'brID=41277344261694034932; cookieyes-consent=consentid:SlExQWtpV0lESUdEVllGbUcyTzJJMk5ZQUtNWElQZlA,consent:yes,action:no,necessary:yes,functional:yes,analytics:yes,performance:yes,advertisement:yes,other:yes,lastRenewedDate:1710054739000; G_ENABLED_IDPS=google; amp_6e3626=7Xu4l1Rm4x_oMIvMJKi4HI...1ikeiatct.1ikeiatct.0.0.0; cf_clearance=wBlQQxu1y5xssUl38CI.4eUA_kNr76uhcX2Wuw.wNho-1748248869-1.2.1.1-.si6CAfgmqTeE7RFglzZzvQ2Ieu.vdEs5txuE7t8.kGx4c3.38tWVeXmi37Wiwzi4w_t6MGomD3veYEDl7MbSaqs7BApKfh6Y5FVl9AMWCK9EBHZ5ZNp6xbsZ2XAsO1V0_I0FuxWup_VG.NPMJIShLXUZCJIdeiHB.if0ueu93VaRjd0XP_Gnt3lYxt.neMm_sjxByIAyPSsavasV1xEk5UNNcFq.ARf.Q01ajqozNLGA4pocI0krREXI47ISYLjVgCgZknwdpLd0YBv7G3Maz54v_cigwZe9R4N8ns79GmsDWKb9VLHbQRFXEDfMhEuh6Vrt6wtOYNqxRQcq_3l7YDaLd4oGXeJqHMA.ysnM.g; lastShowFor2FA87318455=2025-05-20; _ga=GA1.1.1613737730.1747807256; _ga_1NKPLGNKKD=GS2.1.s1748246975$o6$g1$t1748248877$j51$l0$h0$dXsp7NYx82Wb6N55Ne7CljZ2wNJ2wV6FiEw; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%2287318455%22%2C%22expiryDate%22%3A%222026-05-26T08%3A41%3A12.515Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%228bEc19RmSRYCMCpE0jpc%22%2C%22expiryDate%22%3A%222026-05-26T08%3A41%3A12.515Z%22%7D; _clck=nv0xay%7C2%7Cfw8%7C1%7C1967; intercom-session-k4hq7kcu=eUxCUjl6aGRsQUFXRHhzYTFEeGt1UHZqcGpTRFBpakdCa3g2eXpjWFB4NzZaNlNqdXhFSEpVOHNTZnRxUWVjTXpHSmh0NDRVYVd0MUNxRU1TK2c5ZmFRdHNoRForc3B1Wi9GNHBFMkpCbUU9LS16QlpaOUJNK0xUWCtGckhrcnEzQUh3PT0=--f9abe48ff5367ee4ba0150088bb1f5edc19f6fc2; intercom-device-id-k4hq7kcu=1e0a36b1-4c3f-48d5-8052-4e041017f0d9; _gcl_au=1.1.1661123400.1747829170; user-prefs=locale%20xx%20lang%20en%20geo%20bg; ATL_details=SoMKLUJVzRA%3D; user_login_id0=zLXFguO2R08%3D; user_login_id1=SoMKLUJVzRA%3D; ISLOGGED0=1; SSD0=Gqfpl5%2FpItMHK%2B2RSpko4l4Wq7JyNPC3JXZH621nGzNQ2%2Fh8AVyLN9EthROiZAxD%40%40%40be2c6ff9a0a40454; MSESID0=423734971230556646107%2C87318455%2C2%2C0%2CXMYZ0Q%2C1%2C6%2C3768bba72d40f13055e341e49043b305; BSESINFO0=23%2CQ67MXR%2C423735085%2CZ7W6QO; msgCount=1; _clsk=u3wdnx%7C1748248873272%7C4%7C1%7Cj.clarity.ms%2Fcollect; UADCN=Vwy4JPrU5cG2pIq0JO0sglfUcuGvLnyEHch9cp%2FpSeA%3D%40%40%40efda58cec4e3449e; showUserCompleteProfileBanner=Yes; nav-status=%7B%22prm%22%3A%22upgrade%22%2C%22cart%22%3A0%2C%22appBnr%22%3A1%2C%22emlCnf%22%3A0%2C%22gid%22%3A%222252486%22%7D; section=emp; nav-count=0',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "Priority": "u=0",
                # Requests doesn't support trailers
                # 'TE': 'trailers',
            }
        }
    )

    page = context.new_page()
    page.context.add_cookies(cookies)
    # Go to a protected page
    page.goto("https://www.bayt.com/")

    page.wait_for_timeout(50000)
    page.screenshot(path="logged_in_with_cookies.png")

    browser.close()
