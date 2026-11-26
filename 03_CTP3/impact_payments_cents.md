# Impact note: payments.amount goes from euros to cents

1. **What breaks:** `stg_payments.amount` is used in `fct_orders.refunded_eur`, then `net_revenue_eur`, then `dim_customers.lifetime_net_revenue_eur`. If amounts are x100, refunds are x100 too. We tested it: total net revenue goes from +889,645 € to about -12.2 M€ and around 700 orders become negative. Gross revenue does not change, so nobody sees it on the Sales dashboard.
2. **Owners to warn:** Paul Girard (Finance report for the board), Sara Martin (Sales dashboard that the CEO opens every day) and the Head of Data Science (the churn model would see refunded customers as worth nothing).
3. **Test to add before the change:** on `stg_payments.amount`, a range test (between 0 and 5,000) and a test on the mean (between 50 and 1,000 €), like the GX tests we did in CTP 2. This way the cents batch is stopped at staging (Critical).
4. **Who approves:** Paul Girard approves because he is the owner of `stg_payments`. Karim Benali (Steward) updates the doc, and the unit stays euros with 2 decimals.
5. **What we ask:** the payment team must keep sending euros (or convert before sending). If the unit changes one day, it has to go through a new version of the data contract, not a silent change.
