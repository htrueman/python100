-- Task 3

CREATE OR REPLACE TRIGGER were_changes 
BEFORE 
UPDATE
message_date 
ON message 
WHEN OLD.message_date <> NEW.message_date  
DECLARE 
   msg_text text
BEGIN  
  msg_text := :NEW.message.text  || '\n' || 'were changes';
END;
/


-- Task 5

CREATE OR REPLACE PROCEDURE change_leader
u_email IN type text, leader_meail IN type text
IS 
BEGIN 
  UPDATE user set user_email_leader_fr = leader_email WHERE user_email = u_email;
END change_leader;


-- Task 6

DECLARE
    leader_name users.user_name%type,
    CURSOR c_leader_name (msg_count NUMBER)
    IS
        SELECT user_name
        FROM users join message on users.user_email = message.user_email_author_fk
        WHERE HAVING count(message.user_email_author_fk) = msg_count;
BEGIN
    OPEN c_leader_name(k);
    LOOP
        FETCH c_leader_name INTO leader_name;
        EXIT WHEN c_leader_name%notfound;
        dbms_output.put_line(leader_name);
    END LOOP;
    CLOSE c_leader_name;

END;
/
