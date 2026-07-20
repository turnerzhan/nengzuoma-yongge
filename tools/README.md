# tools/ · 可执行工具

> 纯 Python 标准库（除 EXIF 脚本可选 Pillow）。  
> **含上游勇哥全量工具 + 本产品扩展。**

## 上游全量

```bash
# 保本线
python tools/breakeven.py \
  --daily-revenue 800 --daily-food-cost 250 \
  --rent 8000 --labor 9000 --investment 350000 --category 奶茶

# 快招评分
python tools/quack_score.py \
  --source "抖音广告" --hq-city 济南 \
  --total-fee 580000 --direct-stores 2 --years 1 \
  --promises "零加盟费,6个月回本,总部全包"

# 案例匹配（依赖仓库内 cases/）
python tools/match_case.py --amount 900000 --category 奶茶 --location 县城
```

## 本产品扩展

```bash
# 开店前反推 / 有流水体检 / 房租铁律
python tools/profit_model.py plan --rent 12000 --labor 9000 --investment 600000 --category 汉堡
python tools/profit_model.py run --daily-revenue 800 --daily-food-cost 250 --rent 8000 --labor 9000 --category 奶茶
python tools/profit_model.py iron --rent 10000

# 照片 EXIF GPS（可选 pillow）
python tools/parse_image_location.py photo.jpg
```

公式与强制算账规则见：

- `skill/保本线计算器.md`（上游全量）
- `references/profit-model.md`（扩展）
- `corpus/07-行业常识速查.md`
