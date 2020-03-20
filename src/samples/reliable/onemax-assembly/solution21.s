    .file   "solution.c"
    .text
    .globl  _darwin
    .def    _darwin;        .scl    2;      .type   32;     .endef
_darwin:
LFB17:
    .cfi_startproc
    pushl   %ebp
    .cfi_def_cfa_offset 8
    .cfi_offset 5, -8
    movl    %esp, %ebp
    .cfi_def_cfa_register 5

    movl	$-16722, %eax
    movl	$31715, %ebx
    movl	$-1630, %ecx
    movl	$7292, %edx

    sub %edx, %edx
    shr $243, %edx
    shl $8, %eax
    shl $113, %edx
    cmp %ebx, %ecx
    cmp %ecx, %edx
    jno n18
    and %edx, %ecx
    and %edx, %ecx
    jne n15
    sub %eax, %ebx
    jc n15
n15:
    cmp %ebx, %ebx
    sub %edx, %ecx
    cmp %ecx, %eax
n18:
    sub %ecx, %ebx
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
