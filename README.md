# Khởi tạo VPS tại Linode:

Máy ảo khi thuê tại linode sẽ gồm <br>
/dev/sda <br>
Chúng ta phải thu nhỏ ổ đĩa sda này nhỏ lại còn khoảng tầm 50GB <br>
Phần còn lại mount vào thành sdc <br>
Mua thêm ổ đĩa mở rộng mount thành sdd <br>

Ổ đĩa LVM bao gồm <br>

/dev/sdc : ổ đĩa theo gói package thuê <br>
/dev/sdd : ổ đĩa mở rộng <br>

### Khởi tạo Physical Volume
```
pvcreate /dev/sdc /dev/sdd
```
### Khởi tạo Volume Group
```
vgcreate datavg /dev/sdc /dev/sdd
```
#### Nếu bị lỗi thì chạy
```
pvs -o+pv_used
vgreduce datavg --removemissing --test
vgreduce datavg --removemissing
vgreduce --removemissing datavg --force
```
#### Khởi tạo lại Volume Group sau sửa lỗi
```
vgcreate datavg /dev/sdc /dev/sdd
vgs
```
### Khởi tạo Logical volume
```
lvcreate -l 100%FREE -n datavolume datavg
lvs
```
### Format ổ đĩa mới tạo
```
mkfs.ext4 /dev/datavg/datavolume
```
### mount vào thư mục /home
```
mount /dev/datavg/datavolume /home
```
### mount ổ đĩa lúc khởi động
```
vim /etc/fstab
```
#### insert thêm vào cuối dòng
```
/dev/datavg/datavolume /home    ext4  defaults  0 0
```

# Hướng dẫn resize  ổ đĩa
## Tăng thêm dung lượng: <br>
***For extending Logical volumes we don’t need to unmount the file-system.***
- Truy cập linode và resize volume mở rộng
### Resize ổ đĩa trong máy
```
pvresize /dev/sdd
pvs
lvextend -l +100%FREE /dev/mapper/datavg-datavolume
vgs
pvs
lvs
resize2fs /dev/mapper/datavg-datavolume
df -h
```
## Giảm dung lượng: <br>

***Before starting, it is always good to backup the data.***
- unmount the file system for reducing.
- Check the file system after unmount.
- Reduce the file system.
- Reduce the Logical Volume size than Current size.
- Recheck the file system for error.
- Remount the file-system back to stage.



### Resize ổ đĩa trong máy <br>

```
# unmount
umount -v /dev/mapper/datavg-datavolume
# check the disk
e2fsck -ff /dev/mapper/datavg-datavolume
# resize từ 160G --> 130G, xóa bỏ 30G
resize2fs /dev/mapper/datavg-datavolume 130G

lvreduce -L -19G /dev/mapper/datavg-datavolume
resize2fs /dev/mapper/datavg-datavolume
mount /dev/datavg/datavolume /home
df -h
```
- Truy cập linode và resize volume mở rộng

### Delete vg,lv,pv
```
umount -v /dev/mapper/datavg-datavolume
lvremove /dev/mapper/datavg-datavolume
vgchange -an datavg
vgremove datavg
pvremove /dev/sdd /dev/sdc
lsblk
```
Fast add lvm
```
pvcreate /dev/sdc /dev/sdd
vgcreate datavg /dev/sdc /dev/sdd
lvcreate -l 100%FREE -n datavolume datavg
lvs
mkfs.ext4 /dev/datavg/datavolume
mount /dev/datavg/datavolume /home
vim /etc/fstab
/dev/datavg/datavolume /home    ext4  defaults  0 0
:wq
```
