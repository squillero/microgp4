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

    movl	$23937, %eax
    movl	$-23030, %ebx
    movl	$-3504, %ecx
    movl	$2528, %edx

    jo n15
    shl $193, %edx
    jc n33
    sub %ebx, %edx
    shr $210, %eax
    and %edx, %edx
    shl $77, %edx
    shr $64, %ecx
    add %edx, %eax
    xor %edx, %eax
    cmp %ebx, %edx
    cmp %ebx, %eax
n15:
    jo n24
    and %edx, %eax
    shl $194, %ecx
    jo n32
    xor %eax, %eax
    je n31
    shl $116, %eax
    shl $50, %eax
    shl $85, %ecx
n24:
    ja n25
n25:
    jc n26
n26:
    and %ecx, %ecx
    or %ebx, %ebx
    xor %edx, %ebx
    shr $89, %eax
    xor %edx, %ebx
n31:
    jo n32
n32:
    sub %edx, %ecx
n33:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
