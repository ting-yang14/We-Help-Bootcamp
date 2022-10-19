* Goal:不只要記錄留言按讚的數量，還要紀錄每一個留言的按讚會員是誰，支援以下使用場合：  
  * 可以根據留言編號取得該留言有哪些會員按讚。
  * 會員若是嘗試對留言按讚：要能先檢查是否曾經按過讚，然後才將按讚的數量 +1 並且記錄按讚的會員是誰。
* Try:新增一個table儲存留言的編號和按讚的會員
```
--建立table good包含 id, 被按讚的留言編號, 按讚的會員編號, foreign key確保 table message先有留言編號才能按讚
create table good(
id bigint AUTO_INCREMENT PRIMARY KEY,
message_id bigint not Null,
member_id bigint not Null,
FOREIGN KEY(message_id) REFERENCES message(id)
);
--id, 按讚的留言編號, 按讚的會員
insert into good VALUES(1, 1, 1); 
insert into good VALUES(2, 1, 2);
insert into good VALUES(3, 1, 3);
insert into good VALUES(4, 2, 1);
insert into good VALUES(5, 2, 2);
insert into good VALUES(6, 3, 3);
```
 ![image]
```
-- inner join 列出被按讚的留言資料
select * from message inner join good 
on message.id=good.member_id;
```
```
-- 表現有被按讚的留言編號、留言內容、按讚的會員
select message.id, message.content, good.member_id 
from message inner join good 
on message.id=good.message_id;
```
```
-- 計算留言被讚數
select message.id, count(*) 
from message inner join good 
on message.id=good.message_id 
group by message.id;
```
```
-- 如果沒按過則按讚
insert into good (message_id, member_id)
select * from (select 1, 5) as tmp
where not exists (
    select member_id from good where member_id = 5
);
```
