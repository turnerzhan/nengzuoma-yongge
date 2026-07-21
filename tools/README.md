# tools/ · 可执行工具

「能做吗？勇哥」内置计算与匹配脚本。**纯 Python 标准库**（EXIF 脚本可选 Pillow）。

## 保本线

```bash
python tools/breakeven.py \
  --daily-revenue 800 --daily-food-cost 250 \
  --rent 8000 --labor 9000 --investment 350000 --category 奶茶
```

## 加盟风险分

```bash
python tools/quack_score.py \
  --source "抖音广告" --hq-city 济南 \
  --total-fee 580000 --direct-stores 2 --years 1 \
  --promises "零加盟费,6个月回本,总部全包"
```

## 案例匹配

```bash
python tools/match_case.py --amount 900000 --category 奶茶 --location 县城
```

## 开店前反推 / 铁律

```bash
python tools/profit_model.py plan --rent 12000 --labor 9000 --investment 600000 --category 汉堡
python tools/profit_model.py run --daily-revenue 800 --rent 8000 --labor 9000 --category 奶茶
python tools/profit_model.py iron --rent 10000
```

## 照片 GPS（可选）

```bash
python tools/parse_image_location.py photo.jpg
```

说明文档：`skill/保本线计算器.md` · `references/profit-model.md` · `corpus/07-行业常识速查.md`
