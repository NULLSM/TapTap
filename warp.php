<?php
function gstr($length = 10) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}
function gnum($num = 10) {
    $nums = '0123456789';
    $numsLength = strlen($nums);
    $randomNum = '';
    for ($n = 0; $n < $num; $n++) {
        $randomNum .= $nums[rand(0, $numsLength - 1)];
    }
    return $randomNum;
}

function M(){
  
  $uid=gnum(3);
  $key=gstr(43)."=";
  $install_id=gstr(22);
  $fcm=gstr(134);
  $fcm_token=$install_id.":APA91b".$fcm;
  $referrer="115efd11-8646-45a8-a04f-167c658a96e5";
  
  
  
$url = "https://api.cloudflareclient.com/v0a".$uid."/reg";

$curl = curl_init($url);
curl_setopt($curl, CURLOPT_URL, $url);
curl_setopt($curl, CURLOPT_POST, true);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

$headers = array(
   "CF-Client-Version: a-6.16-2483",
   "Content-Type: application/json",
   "Content-Length: 412",
   "Host: api.cloudflareclient.com",
   "Connection: Keep-Alive",
   "Accept-Encoding: gzip",
   "User-Agent: okhttp/3.12.1",
);
curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
$arr = array('key' =>$key,
            'install_id' => $install_id,
            'fcm_token' => $fcm_token,
            'referrer' => $referrer,
'model' => 'Iphone 13 pro',
'serial_number' => $install_id,
'locale' => 'en_IN');
echo json_encode($arr);
$data=json_encode($arr);





curl_setopt($curl, CURLOPT_POSTFIELDS, $data);

//for debug only!
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);

$resp = curl_exec($curl);
curl_close($curl);
var_dump($resp);
}
for($i=0;$i<10;$i++){
  
}
?>

