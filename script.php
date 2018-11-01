<?php 



if($_POST['username'] == 'michel' && $_POST['password'] == 'admin')
{
    echo '<p style="color: green;">Vous êtes administrateur</p>';
}
else 
{
    echo '<p style="color: red;">Vous êtes un imposteur ! La police vien vous chercher !</p>';
}