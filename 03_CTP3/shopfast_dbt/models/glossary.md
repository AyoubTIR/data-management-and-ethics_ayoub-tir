{% docs gross_revenue %}
**Gross revenue (EUR)** — total amount paid by the customer for an order, VAT included, shipping included, before refunds.
Owner: Head of Sales · Steward: Karim Benali · Status: approved (2026-11-10)
{% enddocs %}

{# TODO (Exercise 3): add the terms net_revenue, active_customer, churned_customer, order, customer #}

{% docs net_revenue %}
**Net revenue (EUR)** — what ShopFast really earns on an order: what the customer paid minus refunds, without VAT (shipping included).

- Formula: `(gross_revenue_eur - refunded_eur) / 1.20` (VAT is 20%)
- Example: the customer pays 120 € and gets no refund → 100 €. He pays 120 € and gets 24 € back → 80 €.
- Different from gross revenue (with VAT), which is used for Sales commissions.

Owner: Paul Girard (Head of Finance) · Steward: Karim Benali · Status: approved (2026-11-25)
{% enddocs %}

{% docs active_customer %}
**Active customer** — a customer with at least one order not cancelled in the last 12 months. This is the number given to the board.

- Rule: status is not cancelled and order_date is in the last 12 months
- Example: on 2026-11-25, a customer with a delivered order on 2026-03-10 is active. If his only order was cancelled, he is not.
- Careful: `dim_customers.last_order_date` includes cancelled orders, so it is not enough.
- For the 6 months view, use *recently active customer*.

Owner: Paul Girard (Head of Finance) · Steward: Karim Benali · Status: approved (2026-11-25, decided by the CDO)
{% enddocs %}

{% docs recently_active_customer %}
**Recently active customer** — a customer with at least one order not cancelled in the last 6 months. Used by Sales for campaigns, not for the board.

- Rule: same as active customer but with 6 months.
- Example: on 2026-11-25, a customer with an order on 2026-07-01 is recently active (and also active).

Owner: Sara Martin (Head of Sales) · Steward: Karim Benali · Status: approved (2026-11-25)
{% enddocs %}

{% docs churned_customer %}
**Churned customer** — a customer who already ordered but has no order (not cancelled) in the last 12 months.

- Rule: at least 1 order not cancelled in the past and not an active customer.
- Example: last order on 2025-06-15 → churned on 2026-11-25. A customer who never ordered is not churned.
- This is what the churn model tries to predict.

Owner: Sara Martin (Head of Sales) · Steward: Karim Benali · Status: approved (2026-11-25)
{% enddocs %}

{% docs customer %}
**Customer** — a customer account on ShopFast (one `customer_id`), even if it never ordered.

- Rule: one row in `dim_customers` = one customer.
- Example: 1,233 accounts after removing exact duplicates. 52 people have 2 accounts, and for now they count as 2 customers.

Owner: Sara Martin (Head of Sales) · Steward: Karim Benali · Status: approved (2026-11-25)
{% enddocs %}

{% docs order %}
**Order** — an order made by a customer on any channel, whatever its status (pending, shipped, delivered, cancelled, returned).

- Rule: one row in `fct_orders` = one order. Each KPI has to say if it removes cancelled orders or not.
- Example: 5,200 orders after removing 7 duplicate order_id.

Owner: Sara Martin (Head of Sales) · Steward: Karim Benali · Status: approved (2026-11-25)
{% enddocs %}
