def explanation():
    # 説明を見やすくするためのHTMLコード
    styled_html = """
    <div style="border: 2px solid #4CAF50; border-radius: 15px; padding: 20px; background-color: #f0f8ff; font-family: 'Arial', sans-serif;">
        <h2 style="color: #4CAF50; text-align: center; margin-bottom: 20px; font-family: 'Arial', sans-serif;">📚 コラッツの問題（コラッツ予想）とは？</h2>
        <p style="font-size: 18px; line-height: 1.8; text-align: justify; background-color: #ffffff; padding: 10px; border-radius: 10px; margin-bottom: 20px; font-family: 'Arial', sans-serif;">
            コラッツの問題（コラッツ予想）とは、<strong>どんな正の整数に対しても以下の操作を続けていけば必ず1になる</strong>という未解決問題です。
        </p>
        <div style="background-color: #e0f7fa; padding: 15px; border-radius: 10px; margin-bottom: 20px; font-family: 'Arial', sans-serif;">
            <h3 style="font-size: 20px; line-height: 1.8; margin-bottom: 10px; font-family: 'Arial', sans-serif;"><strong>✨ 操作手順：</strong></h3>
            <ul style="font-size: 20px; line-height: 1.8; list-style-type: none; padding: 0; font-family: 'Arial', sans-serif;">
                <li style="margin-bottom: 10px;">🔹 <strong>その数字が偶数なら2で割る。</strong></li>
                <li style="margin-bottom: 10px;">🔹 <strong>その数字が奇数なら3をかけて1を足す。</strong></li>
            </ul>
        </div>
        <p style="font-size: 18px; line-height: 1.8; text-align: justify; background-color: #ffffff; padding: 10px; border-radius: 10px; font-family: 'Arial', sans-serif;">
            例えば、初期値が6の場合：<br>
            <strong>6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1</strong>
        </p>
    </div>
    """
    return styled_html

