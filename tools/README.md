# tools/

唯一工具目录（无 `scripts/` 双份）。

```bash
# 有流水
python tools/breakeven.py --daily-revenue 800 --daily-food-cost 250 \
  --rent 8000 --labor 9000 --investment 350000 --category 奶茶

# 开店前反推
python tools/breakeven.py plan --rent 12000 --labor 9000 \
  --investment 600000 --category 汉堡

# 房租铁律
python tools/breakeven.py iron --rent 10000

# 快招 / 案例
python tools/quack_score.py --source "抖音" --hq-city 台州 \
  --total-fee 600000 --direct-stores 1 --years 0.5 --promises "全国首家"
python tools/match_case.py --amount 600000 --category 汉堡 --location 县城

# 可选：EXIF / Banana 生图
python tools/parse_image_location.py photo.jpg
python tools/gen_banana_assets.py   # 需 BANANA_API_KEY
```
