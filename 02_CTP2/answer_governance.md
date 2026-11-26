# CTP 2 - Point 5

**Which governance safeguard was missing (owner, contract or test)?**

What was missing is a data contract on payments: nobody wrote down that `amount` is in euros with 2 decimals, so the provider could switch to cents without telling anyone. Our tests only checked "not null / unique / allowed values", which is why the cents batch passed. With a range test (0 to 5000) and a test on the mean, the batch would have been blocked before loading (Critical severity). The owner of the data (Finance) should validate this contract.
