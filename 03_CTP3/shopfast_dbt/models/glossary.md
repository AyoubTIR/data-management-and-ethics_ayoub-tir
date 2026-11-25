{% docs gross_revenue %}
**Gross revenue (EUR)** — total amount paid by the customer for an order, VAT included, shipping included, before refunds.
Owner: Head of Sales · Steward: Karim Benali · Status: approved (2026-11-10)
{% enddocs %}

{# TODO (Exercise 3): add the terms net_revenue, active_customer, churned_customer, order, customer #}

{% docs net_revenue %}
**Net revenue (EUR)** — what ShopFast actually earns on an order: the amount paid minus refunds, **excluding VAT**, shipping fees included.

- Formula: `net_revenue_eur = (gross_revenue_eur - refunded_eur) / 1.20` (French VAT 20%)
- Example: customer pays 120.00 EUR, no refund → 100.00 EUR. Pays 120.00 EUR, 24.00 EUR refunded → 80.00 EUR.
- Not to be confused with *gross revenue* (incl. VAT), used for Sales commissions.

Owner: Paul Girard (Head of Finance) · Steward: Karim Benali · Status: approved (2026-11-25)
{% enddocs %}

{% docs active_customer %}
**Active customer** — a customer account with at least one **non-cancelled** order in the **last 12 months**. Official figure of the board report.

- Rule: `status <> 'cancelled' and order_date > current_date - 12 months and order_date <= current_date`
- Example: on 2026-11-25, last non-cancelled order on 2026-03-10 → active. Only order in the period cancelled → not active.
- Warning: `dim_customers.last_order_date` includes cancelled orders, it is not enough on its own.
- Need a 6-month view? Use *recently active customer*.

Owner: Paul Girard (Head of Finance) · Steward: Karim Benali · Status: approved (2026-11-25, CDO arbitration Sales vs Finance)
{% enddocs %}

{% docs recently_active_customer %}
**Recently active customer** — a customer account with at least one **non-cancelled** order in the **last 6 months**. Used by Sales for seasonal campaigns, never in the board report.

- Rule: same as *active customer* with 6 months instead of 12.
- Example: on 2026-11-25, last non-cancelled order on 2026-07-01 → recently active (and active).

Owner: Sara Martin (Head of Sales) · Steward: Karim Benali · Status: approved (2026-11-25)
{% enddocs %}

{% docs churned_customer %}
**Churned customer** — a customer who ordered in the past but has **no non-cancelled order in the last 12 months** (former buyer, no longer active).

- Rule: at least 1 non-cancelled order ever AND NOT *active customer*.
- Example: last non-cancelled order on 2025-06-15 → churned on 2026-11-25. Account that never ordered → not churned.
- Target variable of the churn prediction model.

Owner: Sara Martin (Head of Sales) · Steward: Karim Benali · Status: approved (2026-11-25)
{% enddocs %}

{% docs customer %}
**Customer** — a registered customer account on ShopFast, identified by `customer_id`, whether or not it has ever ordered.

- Rule: one row in `dim_customers` = one customer.
- Example: 1,233 accounts after removing exact duplicates; 52 people own 2 accounts and still count as 2 customers until a merge is decided.

Owner: Sara Martin (Head of Sales) · Steward: Karim Benali · Status: approved (2026-11-25)
{% enddocs %}

{% docs order %}
**Order** — a purchase placed by a customer on any channel, identified by `order_id`, **whatever its status** (pending, shipped, delivered, cancelled, returned).

- Rule: one row in `fct_orders` = one order. Each KPI must say whether it excludes cancelled orders.
- Example: 5,200 orders after removing 7 duplicated order_ids.

Owner: Sara Martin (Head of Sales) · Steward: Karim Benali · Status: approved (2026-11-25)
{% enddocs %}
