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

    movl	$11163, %eax
    movl	$8487, %ebx
    movl	$17929, %ecx
    movl	$-18798, %edx

    shl $53, %ebx
    jno n27
    jnc n26
    add %ebx, %eax
    or %ecx, %eax
    jz n11
    shr $91, %ecx
    xor %eax, %ebx
n11:
    jne n25
    or %edx, %edx
    or %ecx, %eax
    jnc n25
    jz n24
    shr $32, %eax
    jz n23
    xor %eax, %ecx
    shl $44, %ecx
    jo n27
    or %eax, %edx
    shr $112, %ebx
n23:
    shl $151, %ebx
n24:
    shl $191, %eax
n25:
    xor %ebx, %eax
n26:
    add %eax, %edx
n27:
    shr $156, %ebx
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
